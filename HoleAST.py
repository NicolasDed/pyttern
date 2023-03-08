from ast import *


class HoleAST:
    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return repr(self.__str__())


class SimpleHole(HoleAST):
    def __str__(self):
        return 'ANY'


class CompoundHole(HoleAST):
    def __init__(self, body=None):
        self.body = body

    def __str__(self):
        return 'ANY:'
