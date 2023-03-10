from ast import *
import inspect


class HoleAST:
    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return repr(self.__str__())

    def visit(self, ast, matcher):
        raise NotImplementedError()


class SimpleHole(HoleAST):
    def __str__(self):
        return 'ANY'

    def visit(self, ast, matcher):
        return True


class DoubleHole(HoleAST):
    def __str__(self):
        return 'ANY*'

    def visit(self, ast, matcher):
        return True


class CompoundHole(HoleAST):
    def __init__(self, body=None):
        self.body = body

    def __str__(self):
        return 'ANY:'

    def visit(self, ast, matcher):
        if not hasattr(ast, 'body'):
            return False

        return matcher.asts_equal(self.body, ast.body)


class VarHole(HoleAST):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"ANY but same as other {self.name}"

    def visit(self, ast, matcher):
        if self.name in matcher.variables:
            print(f"{self.name} exist")
            return matcher.asts_equal(matcher.variables[self.name], ast)

        elif self.name in matcher.forbidden:
            print(f"{self.name} forbidden")
            if ast in matcher.forbidden[self.name]:
                print(f"{ast} in forbidden")
                return False

        print(f"Set {self.name} at {ast}")
        matcher.variables[self.name] = ast
        return True
