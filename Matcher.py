from copy import deepcopy

import AstWalker
from HoleAST import *
from PatternMatch import PatternMatch
from PyHoleParser import parse_pyhole


def match_files(path_pattern, path_python, match_details=False):
    pattern = parse_pyhole(path_pattern)
    with open(path_python) as file:
        source = file.read()
        python = ast.parse(source, path_python)

    matcher = Matcher()
    res = matcher.match(pattern, python)

    if not match_details:
        return res

    if res:
        return res, matcher.pattern_match
    else:
        return res, matcher.error


class Matcher:
    def __init__(self):
        self.pattern_walker = None
        self.code_walker = None
        self.saved_pattern_walkers = []
        self.saved_code_walkers = []
        self.variables = {}
        self.pattern_match = PatternMatch()
        self.error = None

    def save_walkers_state(self):
        saved_pattern = deepcopy(self.pattern_walker)
        saved_code = deepcopy(self.code_walker)
        self.saved_pattern_walkers.append(saved_pattern)
        self.saved_code_walkers.append(saved_code)

    def load_walkers_state(self):
        saved_pattern = self.saved_pattern_walkers.pop()
        saved_code = self.saved_code_walkers.pop()
        self.pattern_walker = saved_pattern
        self.code_walker = saved_code

    def match(self, pattern, code):
        ast.fix_missing_locations(pattern)
        self.pattern_walker = AstWalker.AstWalker(pattern)
        self.code_walker = AstWalker.AstWalker(code)

        return self.simple_match()

    def simple_match(self):
        pattern_node = self.pattern_walker.next()
        if pattern_node is None:
            code_node = self.code_walker.next()
            if code_node is not None:
                return False
            else:
                return True

        code_node = self.code_walker.next()
        if code_node is None:
            return False

        return self.rec_match(pattern_node, code_node)

    def rec_match(self, pattern_node, code_node):
        if isinstance(pattern_node, HoleAST):
            return pattern_node.visit(self, code_node)

        if type(pattern_node) != type(code_node):
            self.error = f"Cannot match {pattern_node} with {code_node}"
            return False

        if isinstance(pattern_node, AST):
            for const_pattern, const_code in zip(iter_constant_field(pattern_node), iter_constant_field(code_node)):
                if isinstance(const_pattern, SimpleHole):
                    self.pattern_walker.next()
                    continue
                if const_pattern != const_code:
                    if isinstance(const_code, ast.Load) or isinstance(const_code, ast.Store):
                        continue
                    self.error = f"Cannot match const {const_pattern} with {const_code}"
                    return False

        if hasattr(pattern_node, "lineno"):
            self.pattern_match.add_pattern_match(pattern_node.lineno, pattern_node)

        self.pattern_match.add_match(pattern_node, code_node)

        return self.simple_match()
