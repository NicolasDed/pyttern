import glob
from copy import deepcopy

from .ASTMatcher import ASTMatcher
from .AstWalker import AstWalker
from .PatternMatch import PatternMatch
from .PytternAST import *
from .PytternParser import parse_pyttern


def match_wildcards(path_pattern_with_wildcards, path_python_with_wildcard,
                    strict_match=False, match_details=False):
    ret = {}
    patterns_filespath = glob.glob(str(path_pattern_with_wildcards))
    pythons_filespath = glob.glob(str(path_python_with_wildcard))
    for python_filepath in pythons_filespath:
        for pattern_filepath in patterns_filespath:
            result = match_files(pattern_filepath, python_filepath, strict_match, match_details)
            if python_filepath not in ret:
                ret[python_filepath] = {}
            ret[python_filepath][pattern_filepath] = result
    return ret


def match_files(path_pattern, path_python, strict_match=False, match_details=False):
    pattern = parse_pyttern(path_pattern)
    with open(path_python, encoding="utf-8") as file:
        source = file.read()
        python = ast.parse(source, path_python)

    matcher = Matcher()
    matcher.set_strict(strict_match)
    res = matcher.match(pattern, python)

    if not match_details:
        return res

    if res:
        return res, matcher.pattern_match

    return res, matcher.error


class Matcher:
    def __init__(self):
        self.pattern_walker: AstWalker = None
        self.code_walker: AstWalker = None
        self.saved_pattern_walkers = []
        self.saved_code_walkers = []
        self.saved_patten_matches = []
        self.variables = {}
        self.pattern_match = PatternMatch()
        self.error = None
        self.strict = True

    def set_strict(self, strict):
        self.strict = strict

    def save_walkers_state(self):
        saved_pattern = deepcopy(self.pattern_walker)
        saved_code = deepcopy(self.code_walker)
        saved_match = deepcopy(self.pattern_match)
        self.saved_pattern_walkers.append(saved_pattern)
        self.saved_code_walkers.append(saved_code)
        self.saved_patten_matches.append(saved_match)

    def load_walkers_state(self):
        saved_pattern = self.saved_pattern_walkers.pop()
        saved_code = self.saved_code_walkers.pop()
        saved_match = self.saved_patten_matches.pop()
        self.pattern_walker = saved_pattern
        self.code_walker = saved_code
        self.pattern_match = saved_match

    def drop_walkers_state(self):
        self.saved_pattern_walkers.pop()
        self.saved_code_walkers.pop()
        self.saved_patten_matches.pop()

    def match(self, pattern, code):
        ast.fix_missing_locations(pattern)
        self.pattern_walker = AstWalker(pattern)
        self.code_walker = AstWalker(code)

        pattern_node = self.pattern_walker.current()
        code_node = self.code_walker.current()
        if pattern_node is None:
            if not self.strict:
                return True
            if code_node is not None:
                return False

            return True

        if code_node is None:
            return False

        if self.strict:
            return self.strict_rec_match(pattern_node, code_node)

        return self.soft_rec_match(pattern_node, code_node)

    def simple_match(self):
        pattern_node = self.pattern_walker.next()
        if pattern_node is None:
            if not self.strict:
                return True
            code_node = self.code_walker.next()
            if code_node is not None:
                return False

            return True

        code_node = self.code_walker.next()
        if code_node is None:
            return False

        if self.strict:
            return self.strict_rec_match(pattern_node, code_node)

        return self.soft_rec_match(pattern_node, code_node)

    def rec_match(self, pattern, code):
        if self.strict:
            return self.strict_rec_match(pattern, code)
        else:
            return self.soft_rec_match(pattern, code)

    def match_soft(self, pattern, code):
        ast.fix_missing_locations(pattern)
        self.pattern_walker = AstWalker(pattern)
        self.code_walker = AstWalker(code)

        return self.simple_match()

    def soft_next_node_match(self, pattern_node):
        next_code_node = self.code_walker.next_sibling()
        if next_code_node is None:
            self.error = f"No next match node for {pattern_node}"
            return False
        return self.soft_rec_match(pattern_node, next_code_node)

    def soft_rec_match(self, pattern_node, code_node):
        if isinstance(pattern_node, PytternAST):
            self.save_walkers_state()
            if not pattern_node.visit(self, code_node):
                self.load_walkers_state()
                return self.soft_next_node_match(pattern_node)
            self.drop_walkers_state()
            return True

        if isinstance(pattern_node, AST):
            matcher = ASTMatcher(self)
            self.save_walkers_state()
            if not matcher.visit(pattern_node, code_node):
                self.load_walkers_state()
                return self.soft_next_node_match(pattern_node)
            self.drop_walkers_state()
        elif type(pattern_node) != type(code_node):
            return self.soft_next_node_match(pattern_node)

        if not isinstance(pattern_node, (AST, PytternAST, list)):
            if pattern_node == code_node:
                return self.simple_match()
            else:
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

        return True

    def match_strict(self, pattern, code):
        ast.fix_missing_locations(pattern)
        self.pattern_walker = AstWalker(pattern)
        self.code_walker = AstWalker(code)

        return self.simple_match()

    def strict_rec_match(self, pattern_node, code_node):
        if isinstance(pattern_node, PytternAST):
            return pattern_node.visit(self, code_node)

        if type(pattern_node) != type(code_node):
            self.error = f"Cannot match {pattern_node} with {code_node}"
            return False

        if not isinstance(pattern_node, (AST, PytternAST, list)):
            if pattern_node == code_node:
                return self.simple_match()
            else:
                self.error = f"Cannot match constant {pattern_node} and {code_node}."
                return False

        if hasattr(code_node, "lineno") and hasattr(pattern_node, "lineno"):
            self.pattern_match.add_pattern_match(code_node.lineno, pattern_node)

        self.pattern_match.add_match(pattern_node, code_node)
        self.pattern_match.match(code_node, pattern_node)

        return self.simple_match()