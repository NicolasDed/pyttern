import ast
from HoleAST import *


class Matcher:

    def __init__(self):
        self.variables = {}
        self.forbidden = {}


    def setVariable(self, name, ast):
        self.variables[name] = ast

    def match(self, pattern, code):
        while True:
            mat = self.asts_equal(pattern, code)
            if mat:
                return True
            if len(self.variables) == 0:
                return False
            for key, val in self.variables.items():
                if key not in self.forbidden:
                    self.forbidden[key] = []
                self.forbidden[key].append(val)
            self.variables = {}

    def asts_equal(self, expected_ast, actual_ast):
        """
        Compare two abstract syntax trees (ASTs) to see if they are equal.
        """
        if isinstance(expected_ast, HoleAST):
            return self.matchHole(expected_ast, actual_ast)

        if isinstance(expected_ast, ast.Load) and isinstance(actual_ast, ast.Store) \
                or isinstance(expected_ast, ast.Store) and isinstance(actual_ast, ast.Load):
            return True

        if type(expected_ast) != type(actual_ast):
            print(f"Invalid types {type(expected_ast)} != {type(actual_ast)}")
            return False

        if isinstance(expected_ast, ast.AST):
            for field, expected_value in ast.iter_fields(expected_ast):
                actual_value = getattr(actual_ast, field, None)
                if not self.asts_equal(expected_value, actual_value):
                    print(f"Invalid attrs {expected_value} != {actual_value}")
                    return False
            return True

        elif isinstance(expected_ast, list):
            if len(actual_ast) == 0 and len(expected_ast) == 0:
                return True

            return self.matchListWithHole(expected_ast, actual_ast)

        else:
            return expected_ast == actual_ast

    def matchListWithHole(self, expected_list, actual_list):
        if len(expected_list) == 0 and len(actual_list) == 0:
            return True

        if len(expected_list) == 0 and len(actual_list) > 0:
            return False

        first_val = expected_list[0]
        if isinstance(first_val, DoubleHole):
            return self.matchAnyInList(expected_list, actual_list)
        else:
            if not self.asts_equal(first_val, actual_list[0]):
                print(f"Error in list {first_val} != {actual_list[0]}")
                return False

            return self.matchListWithHole(expected_list[1:], actual_list[1:])

    def matchAnyInList(self, expected_list, actual_list):
        # Find index of first non-hole
        index = -1
        for i, val in enumerate(expected_list):
            if not isinstance(val, DoubleHole):
                index = i
                break

        # no more values
        if index == -1:
            return len(actual_list) == 0 or len(expected_list) != 0

        toFind = expected_list[index]
        start = 0
        found = False
        while not found:
            indexFound = self.findFirst(toFind, actual_list, start)
            if indexFound == -1:
                print(f"{toFind} not found in {actual_list}")
                return False
            else:
                indexFound += start
                if self.matchListWithHole(expected_list[index + 1:], actual_list[indexFound + 1:]):
                    return True

            print("backtrack")
            start = indexFound + 1

    def findFirst(self, AstToFind, AstList, start=0):
        print(f'Search {AstToFind} in {AstList[start:]}')
        if start >= len(AstList):
            return -1
        for i, val in enumerate(AstList[start:]):
            if self.asts_equal(AstToFind, val):
                return i
        return -1

    def matchHole(self, expected_ast, actual_ast):
        return expected_ast.visit(actual_ast, self)
