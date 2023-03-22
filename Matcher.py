from copy import deepcopy

import AstWalker
from HoleAST import *
from PyHoleParser import parse_pyhole


def match_files(path_pattern, path_python):
    pattern = parse_pyhole(path_pattern)
    python = parse_pyhole(path_python)

    res = Matcher().match(pattern, python)

    return res


class Matcher:
    def __init__(self):
        self.pattern_walker = None
        self.code_walker = None
        self.saved_pattern_walkers = []
        self.saved_code_walkers = []
        self.variables = {}

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
            return False

        if isinstance(pattern_node, AST):
            for const_pattern, const_code in zip(iter_constant_field(pattern_node), iter_constant_field(code_node)):
                if const_pattern != const_code:
                    return False

        return self.simple_match()
