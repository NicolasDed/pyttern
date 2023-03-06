from unittest import TestCase
import io
import ast

import pytest
from antlr4 import *
from antlr4.error.ErrorListener import *

from antlr.Python3Lexer import Python3Lexer
from antlr.Python3Parser import Python3Parser
from antlr.Python3Listener import Python3Listener

from Python3Visitor import Python3Visitor


class Python3ErrorListener(ErrorListener):
    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offendingSymbol.text
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: {}".format(str(stack)))
        print("line {} : {} at {} : {}".format(str(line),
                                               str(column),
                                               str(offendingSymbol).replace(" ", u'\u23B5'),
                                               msg.replace(" ", u'\u23B5')))

    @property
    def symbol(self):
        return self._symbol

class Printer(ParseTreeListener):
    def __init__(self):
        self.depth = 0

    def enterEveryRule(self, ctx):
        print((self.depth*' ') + type(ctx).__name__)
        self.depth += 1

    def exitEveryRule(self, ctx):
        self.depth -= 1

    def visitTerminal(self, node:TerminalNode):
        print(node)


class Python3ParserTests(TestCase):

    def setup(self, path):
        input = FileStream(path, encoding="utf-8")
        lexer = Python3Lexer(input)
        stream = CommonTokenStream(lexer)

        # print out the token parsing
        """stream.fill()
        print("TOKENS")
        for token in stream.tokens:
            if token.text != '<EOF>':
                type_name = Python3Parser.symbolicNames[token.type]
                tabs = 5 - len(type_name) // 4
                sep = "\t" * tabs
                print("    %s%s%s" % (type_name, sep,
                                      token.text.replace(" ", u'\u23B5').replace("\n", u'\u2936')))"""
        parser = Python3Parser(stream)
 
        self.output = io.StringIO()
        self.error = io.StringIO()

        parser.removeErrorListeners()
        self.errorListener = Python3ErrorListener(self.error)
        parser.addErrorListener(self.errorListener)
        return parser

    def test_python3_test_grammar(self):
        parser = self.setup("test/test_grammar.py")
        tree = parser.file_input()
        listener = Python3Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        self.assertEqual(len(self.errorListener.symbol), 0)

    def test_python3_test_student(self):
        parser = self.setup("test/q1_3.py")
        tree = parser.file_input()
        listener = Printer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        self.assertEqual(len(self.errorListener.symbol), 0)



class AstGeneratorTests(TestCase):

    def setup(self, path):
        input = FileStream(path, encoding="utf-8")
        lexer = Python3Lexer(input)
        stream = CommonTokenStream(lexer)
        parser = Python3Parser(stream)
 
        self.output = io.StringIO()
        self.error = io.StringIO()

        parser.removeErrorListeners()
        self.errorListener = Python3ErrorListener(self.error)
        parser.addErrorListener(self.errorListener)
        return parser

    def asts_equal(self, expected_ast, actual_ast):
        """
        Compare two abstract syntax trees (ASTs) to see if they are equal.
        """
        self.__asts_equal(expected_ast, actual_ast, [])

    def __asts_equal(self, expected_ast, actual_ast, path):
        """
        Compare two abstract syntax trees (ASTs) to see if they are equal.
        """
        if hasattr(actual_ast, 'name'):
            toApp = (type(actual_ast).__name__, actual_ast.name)
        else:
            toApp = type(actual_ast).__name__
        path.append(toApp)

        if isinstance(expected_ast, ast.Load) and isinstance(actual_ast, ast.Store) \
            or isinstance(expected_ast, ast.Store) and isinstance(actual_ast, ast.Load):
            path.pop()
            return

        self.assertEqual(type(actual_ast), type(expected_ast), (actual_ast, expected_ast, path))

        if isinstance(expected_ast, ast.AST):
            for field, expected_value in ast.iter_fields(expected_ast):
                path.append(field)
                actual_value = getattr(actual_ast, field, None)
                self.__asts_equal(expected_value, actual_value, path)
                path.pop()

        elif isinstance(expected_ast, list):
            self.assertEqual(len(actual_ast), len(expected_ast), f"{str(actual_ast)} != {str(expected_ast)} : {path}")
            for expected_value, actual_value in zip(expected_ast, actual_ast):
                self.__asts_equal(expected_value, actual_value, path)

        else:
            self.assertEqual(actual_ast, expected_ast, path)
                
        
        path.pop()

    def test_ast_generator_student(self):
        parser = self.setup("test/q1_3.py")
        tree = parser.file_input()
        
        generatedTree = Python3Visitor().visit(tree)
        print(ast.dump(generatedTree, indent=1))

        with open("test/q1_3.py") as file:
            pythonTree = ast.parse(file.read(), "test/q1_3.py")
            print()
            print(ast.dump(pythonTree, indent=1))
            self.asts_equal(pythonTree, generatedTree)

    def test_ast_generator_student2(self):
        parser = self.setup("test/q1_254.py")
        tree = parser.file_input()
        
        generatedTree = Python3Visitor().visit(tree)
        print(ast.dump(generatedTree, indent=1))

        with open("test/q1_254.py") as file:
            pythonTree = ast.parse(file.read(), "test/q1_254.py")
            print()
            print(ast.dump(pythonTree, indent=1))
            self.asts_equal(pythonTree, generatedTree)


    def test_ast_generator_complex(self):
        parser = self.setup("test/test_grammar.py")
        tree = parser.file_input()
        
        generatedTree = Python3Visitor().visit(tree)
        print(ast.dump(generatedTree, indent=1))


        with open("test/test_grammar.py") as file:
            pythonTree = ast.parse(file.read(), "test/test_grammar.py")
            print()
            print(ast.dump(pythonTree, indent=1))
            self.asts_equal(pythonTree, generatedTree)