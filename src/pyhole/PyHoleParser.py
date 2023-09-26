import argparse
import io

from antlr4 import FileStream, CommonTokenStream, ParseTreeListener, TerminalNode, ParseTreeWalker

from .PyHoleErrorListener import Python3ErrorListener
from .PyHoleVisitor import PyHoleVisitor
from .antlr.Python3Lexer import Python3Lexer
from .antlr.Python3Parser import Python3Parser


class Printer(ParseTreeListener):
    def __init__(self):
        self.depth = 0

    def enterEveryRule(self, ctx):
        print((self.depth * ' ') + type(ctx).__name__)
        self.depth += 1

    def exitEveryRule(self, ctx):
        self.depth -= 1

    def visitTerminal(self, node: TerminalNode):
        print((self.depth * ' ') + str(node))


def _parse_pyhole_to_antlr(path):
    file_input = FileStream(path, encoding="utf-8")
    lexer = Python3Lexer(file_input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)

    error = io.StringIO()

    parser.removeErrorListeners()
    error_listener = Python3ErrorListener(error)
    parser.addErrorListener(error_listener)
    tree = parser.file_input()
    if len(error_listener.symbol) > 0:
        raise IOError(f"Syntax error in {path} at line {error_listener.line} "
                      f"({repr(error_listener.symbol)}) : {error.getvalue()}")

    return tree


def parse_pyhole(path):
    tree = _parse_pyhole_to_antlr(path)

    generated_tree = PyHoleVisitor().visit(tree)
    return generated_tree


def main(args):
    if args.brut:
        print(args.pytternFile)
        tree = _parse_pyhole_to_antlr(args.pytternFile)
        listener = Printer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    elif args.codeFile:
        from .Matcher import match_files
        print(match_files(args.pytternFile, args.codeFile))

    else:
        print(parse_pyhole(args.pytternFile))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Pyttern',
        description='Parse Pyttern code')

    exclusive_group = parser.add_mutually_exclusive_group()

    exclusive_group.add_argument('-b', '--brut',
                                 action='store_true')
    parser.add_argument("pytternFile")
    exclusive_group.add_argument("-c", "--codeFile", required=False)

    args = parser.parse_args()
    main(args)
