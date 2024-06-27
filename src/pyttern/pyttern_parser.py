"""
Main module for the Pyttern parser.
"""

import io
import tempfile
from ast import dump
from ast import parse
from functools import cache

from antlr4 import FileStream, CommonTokenStream, ParseTreeListener, TerminalNode, ParseTreeWalker

from .antlr.Python3Lexer import Python3Lexer
from .antlr.Python3Parser import Python3Parser
from .pyttern_error_listener import Python3ErrorListener


class Printer(ParseTreeListener):
    """
    This class is a custom listener that extends the ParseTreeListener class provided by ANTLR.
    It is used to walk through the parse tree and print the tree structure.

    Attributes:
    depth (int): The current depth in the parse tree. This is used for indentation when printing the tree structure.
    """

    def __init__(self):
        """
        The constructor for the Printer class. It initializes the depth to 0.
        """
        self.depth = 0

    def enterEveryRule(self, ctx):
        """
        This method is called when entering every rule in the parse tree.
        It prints the name of the rule and increases the depth by 1.

        Parameters:
        ctx (ParserRuleContext): The context of the rule being entered.
        """
        print((self.depth * ' ') + type(ctx).__name__)
        self.depth += 1

    def exitEveryRule(self, ctx):
        """
        This method is called when exiting every rule in the parse tree.
        It decreases the depth by 1.

        Parameters:
        ctx (ParserRuleContext): The context of the rule being exited.
        """
        self.depth -= 1

    def visitTerminal(self, node: TerminalNode):
        """
        This method is called when visiting a terminal node in the parse tree.
        It prints the terminal node.

        Parameters:
        node (TerminalNode): The terminal node being visited.
        """
        print((self.depth * ' ') + str(node))


def _parse_pyttern_to_antlr(path):
    """
    This function takes a path to a Python file as input, parses the file into an ANTLR parse tree,
    and returns the parse tree. It also handles syntax errors in the Python file.

    Parameters:
    path (str): The path to the Python file to parse.

    Returns:
    ParseTree: The ANTLR parse tree representation of the Python file.

    Raises:
    IOError: If there is a syntax error in the Python file.
    """
    file_input = FileStream(path, encoding="utf-8")
    lexer = Python3Lexer(file_input)
    stream = CommonTokenStream(lexer)
    py_parser = Python3Parser(stream)

    error = io.StringIO()

    py_parser.removeErrorListeners()
    error_listener = Python3ErrorListener(error)
    py_parser.addErrorListener(error_listener)
    tree = py_parser.file_input()
    if len(error_listener.symbol) > 0:
        raise IOError(f"Syntax error in {path} at line {error_listener.line} "
                      f"({repr(error_listener.symbol)}) : {error.getvalue()}")

    return tree


@cache
def parse_pyttern(path):
    """
    This function takes a path to a Python file as input, parses the file into an ANTLR parse tree,
    then transforms the parse tree into a Pyttern Abstract Syntax Tree (AST) using the PytternVisitor class.

    Parameters:
    path (str): The path to the Python file to parse.

    Returns:
    Pyttern AST: The Pyttern AST representation of the Python file.
    """
    with open(path, encoding="utf-8") as file:
        source = file.read()
        splitted = source.split('!#')
        patterns = {}
        for slit in splitted:
            name, code = slit.split('\n', 1)
            with tempfile.TemporaryFile() as temp:
                temp.write(code.encode())
                tree = _parse_pyttern_to_antlr(temp)
                patterns[name.strip()] = tree
        return patterns

    # tree = _parse_pyttern_to_antlr(path)
    #
    # generated_tree = PytternVisitor().visit(tree)
    # return generated_tree


@cache
def parse_python(path):
    with open(path, encoding="utf-8") as file:
        source = file.read()
        python = parse(source, path)
    return python


def main(args):
    """
    This is the main function of the program. It takes command line arguments as input and performs different actions
    based on the arguments.

    If the 'brut' argument is provided, it prints the path to the Pyttern file, parses the file into an ANTLR parse tree,
    then walks the parse tree using a Printer listener to print the tree.

    If the 'codeFile' argument is provided, it matches the Pyttern file with the code file and prints the result.

    If neither 'brut' nor 'codeFile' is provided, it parses the Pyttern file into a Pyttern AST and prints the AST.

    Parameters:
    args (argparse.Namespace): The command line arguments.
    """
    if args.brut:
        print(args.pytternFile)
        tree = _parse_pyttern_to_antlr(args.pytternFile)
        listener = Printer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    elif args.codeFile:
        from .matcher import match_files
        print(match_files(args.pytternFile, args.codeFile))

    else:
        parsed = parse_pyttern(args.pytternFile)
        for name in parsed:
            print(dump(parsed[name], indent=" "))