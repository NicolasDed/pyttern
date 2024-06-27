"""
Main module for matching patterns with python code.
Describe the main Matcher class and the match functions.
"""
import ast
import glob
from copy import copy

from .ast_walker import ast_walker
from .astmatcher import AstMatcher
from .astpyttern import AstPyttern
from .pattern_match import PatternMatch
from .pyttern_parser import parse_pyttern, parse_python

try:
    from tqdm import tqdm
except ImportError:
    pass


def match_wildcards(path_pattern_with_wildcards: str, path_python_with_wildcard: str,
                    strict_match=False, match_details=False, count=False):
    """
    Match all python files with all pattern files.
    The path_pattern_with_wildcards and path_python_with_wildcard
    can contain wildcards. The function returns a dictionary with the results of the matches.
    :param path_pattern_with_wildcards: Path to the pattern files with wildcards.
    :param path_python_with_wildcard: Path to the python files with wildcards.
    :param strict_match: If True, the match will be strict, otherwise it will be soft.
    :param match_details: If True, the function will return the match details.
    :param count: If True, the function will return the number of matches.
    :param n_threads: Number of threads to use.
    :return: Dictionary with the results of the matches.
    """

    ret = {}
    patterns_filespath = glob.glob(str(path_pattern_with_wildcards))
    pythons_filespath = glob.glob(str(path_python_with_wildcard))

    try:
        pythons_filespath = tqdm(pythons_filespath)
    except NameError:
        pass

    for python_filepath in pythons_filespath:
        for pattern_filepath in patterns_filespath:
            result = match_files(pattern_filepath, python_filepath, strict_match, match_details, count)
            if python_filepath not in ret:
                ret[python_filepath] = {}
            ret[python_filepath][pattern_filepath] = result
    return ret


def match_files(path_pattern, path_python, strict_match=False, match_details=False, count=False):
    """
    Match a pattern file with a python file.
    :param path_pattern: Path to the pattern file.
    :param path_python: Path to the python file.
    :param strict_match: If True, the match will be strict, otherwise it will be soft.
    :param match_details: If True, the function will return the match details.
    :param count: If True, the function will return the number of matches.
    :return: The result of the match.
    """

    pattern = parse_pyttern(path_pattern)
    python = parse_python(path_python)

    matcher = Matcher()
    matcher.set_strict(strict_match)
    matcher.count = count
    res = matcher.match(pattern, python)

    if count:
        if match_details:
            if matcher.counter > 0:
                return matcher.counter > 0, matcher.counter, matcher.true_pattern_matches
            return matcher.counter > 0, matcher.counter, matcher.error
        return matcher.counter > 0, matcher.counter

    if not match_details:
        return res

    if res:
        return res, matcher.pattern_match

    return res, matcher.error


class Matcher:
    """
    Main class for matching patterns with python code. It contains the main algorithms for matching.
    This class go through both ast trees and try to match them. It uses the ast_walker class to
    keep track of the current nodes in the trees, the ast_matcher class to match ast nodes between
    them and the pyttern_ast class to match pyttern nodes with ast nodes.
    """

    def __init__(self):
        """
        Constructor for Matcher class.
        """
        self.pattern_walker = None
        self.code_walker = None
        self.pattern_match = PatternMatch()
        self.saved_pattern_walkers = []
        self.saved_code_walkers = []
        self.saved_pattern_matches = []
        self.true_pattern_matches = []
        self.variables = {}
        self.error = None
        self.strict = True
        self.count = False
        self.counter = 0

    def set_strict(self, strict: bool):
        """Switch the matching to strict or soft."""
        self.strict = strict

    def save_walkers_state(self):
        """
        Save the current state of the walkers and the pattern match for backtracking.
        """
        # saved_pattern = self.pattern_walker.copy()
        # saved_code = self.code_walker.copy()
        # saved_match = self.pattern_match.copy()
        saved_pattern = copy(self.pattern_walker)
        saved_code = copy(self.code_walker)
        saved_match = copy(self.pattern_match)
        self.saved_pattern_walkers.append(saved_pattern)
        self.saved_code_walkers.append(saved_code)
        self.saved_pattern_matches.append(saved_match)

    def load_walkers_state(self):
        """
        Load the last saved state of the walkers and the pattern match when backtracking.
        """
        saved_pattern = self.saved_pattern_walkers.pop()
        saved_code = self.saved_code_walkers.pop()
        saved_match = self.saved_pattern_matches.pop()
        self.pattern_walker = saved_pattern
        self.code_walker = saved_code
        self.pattern_match = saved_match

    def drop_walkers_state(self):
        """
        Drop the last saved state of the walkers and the pattern match when cutting the search tree.
        """
        self.saved_pattern_walkers.pop()
        self.saved_code_walkers.pop()
        self.saved_pattern_matches.pop()

    def match(self, pattern, code) -> bool:
        """
        Main method for matching patterns with python code.
        :param pattern: Pattern to be matched.
        :param code: Code to be matched.
        :return: True if the pattern matches the code, False otherwise.
        """
        ast.fix_missing_locations(pattern)
        self.pattern_walker = ast_walker(pattern)
        self.code_walker = ast_walker(code)

        pattern_node = self.pattern_walker.current()
        code_node = self.code_walker.current()
        if pattern_node is None:
            if not self.strict:
                return self.count_and_return()
            if code_node is not None:
                return False

            return self.count_and_return()

        if code_node is None:
            return False

        if self.strict:
            return self.strict_rec_match(pattern_node, code_node)

        return self.soft_rec_match(pattern_node, code_node)

    def simple_match(self) -> bool:
        """
        Yield the next nodes from the pattern and the code and perform simple matching steps.
        This method checks if we are at the end of the pattern or the code and if we are not,
        it calls the strict or soft matching methods.
        """
        pattern_node = self.pattern_walker.next()
        if pattern_node is None:
            if not self.strict:
                return self.count_and_return()
            code_node = self.code_walker.next()
            if code_node is not None:
                return False

            return self.count_and_return()

        code_node = self.code_walker.next()
        if code_node is None:
            return False

        if self.strict:
            return self.strict_rec_match(pattern_node, code_node)

        return self.soft_rec_match(pattern_node, code_node)

    def rec_match(self, pattern, code):
        """
        Choose the matching method based on the strict attribute.
        """
        if self.strict:
            return self.strict_rec_match(pattern, code)

        return self.soft_rec_match(pattern, code)

    def soft_next_node_match(self, pattern_node):
        """
        Yield the next node from the code if the soft matching fails.
        """
        next_code_node = self.code_walker.next_sibling()
        if next_code_node is None:
            self.error = f"No next match node for {pattern_node}"
            return False
        return self.soft_rec_match(pattern_node, next_code_node)

    def count_and_return(self):
        if self.count:
            self.true_pattern_matches.append(self.pattern_match)
            self.counter += 1
            return False
        return True

    def soft_rec_match(self, pattern_node, code_node):
        """
        Recursive matching method for soft matching.
        Check if both nodes match and if they do, continue the matching process.
        Else, return False to go back to the closest backtracking point.
        :param pattern_node: Pattern node to be matched.
        :param code_node: Code node to be matched.
        :return: True if the pattern matches the code, False otherwise.
        """

        # If we try to match a Pyttern node, we delegate the matching to the Pyttern class.
        if isinstance(pattern_node, AstPyttern):
            self.save_walkers_state()
            if not pattern_node.visit(self, code_node):
                self.load_walkers_state()
                return self.soft_next_node_match(pattern_node)
            self.drop_walkers_state()
            if self.count:
                self.counter += 1
                return False
            return self.count_and_return()

        # If we try to match an AST node, we delegate the matching to the ast_matcher class.
        if isinstance(pattern_node, ast.AST):
            matcher = AstMatcher(self)
            self.save_walkers_state()
            if not matcher.visit(pattern_node, code_node):
                self.load_walkers_state()
                return self.soft_next_node_match(pattern_node)
            self.drop_walkers_state()
        elif type(pattern_node) is not type(code_node):
            return self.soft_next_node_match(pattern_node)

        # Lists should be handled differently.
        if not isinstance(pattern_node,  (list, ast.AST)):
            if pattern_node == code_node:
                return self.simple_match()

            self.error = f"Cannot match constant {pattern_node} and {code_node}."
            return False

        if hasattr(code_node, "lineno") and hasattr(pattern_node, "lineno"):
            self.pattern_match.add_pattern_match(code_node.lineno, pattern_node)

        self.pattern_match.add_match(pattern_node, code_node)
        self.pattern_match.match(code_node, pattern_node)

        self.save_walkers_state()
        if not self.simple_match():
            self.load_walkers_state()
            return self.soft_next_node_match(pattern_node)
        self.drop_walkers_state()

        return self.count_and_return()

    def strict_rec_match(self, pattern_node, code_node):
        """
        Recursive matching method for strict matching.
        Check if both nodes match and if they do, continue the matching process.
        Else, return False.
        :param pattern_node: Pattern node to be matched.
        :param code_node: Code node to be matched.
        :return: True if the pattern matches the code, False otherwise.
        """
        # If we try to match a Pyttern node, we delegate the matching to the Pyttern class.
        if isinstance(pattern_node, AstPyttern):
            return pattern_node.visit(self, code_node)

        # If we try to match an AST node, we delegate the matching to the ast_matcher class.
        # TODO: doesnt delegate to ast_matcher but should
        if type(pattern_node) is not type(code_node):
            self.error = f"Cannot match {pattern_node} with {code_node}"
            return False

        if not isinstance(pattern_node, (list, ast.AST)):
            if pattern_node == code_node:
                return self.simple_match()

            self.error = f"Cannot match constant {pattern_node} and {code_node}."
            return False

        if hasattr(code_node, "lineno") and hasattr(pattern_node, "lineno"):
            self.pattern_match.add_pattern_match(code_node.lineno, pattern_node)

        self.pattern_match.add_match(pattern_node, code_node)
        self.pattern_match.match(code_node, pattern_node)

        return self.simple_match()
