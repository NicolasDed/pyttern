from ast import *


class HoleAST:
    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return repr(self.__str__())


class Hole(HoleAST):
    def __init__(self):
        self._fields = []

    def __str__(self):
        return 'ANY'
