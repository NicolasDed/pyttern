import ast
from unittest import TestCase

import pytest
from antlr4 import *

from Matcher import Matcher, match_files
from PyHoleParser import *
from antlr.Python3Lexer import Python3Lexer
from antlr.Python3Listener import Python3Listener
from antlr.Python3Parser import Python3Parser


class Printer(ParseTreeListener):
    def __init__(self):
        self.depth = 0

    def enterEveryRule(self, ctx):
        print((self.depth * ' ') + type(ctx).__name__)
        self.depth += 1

    def exitEveryRule(self, ctx):
        self.depth -= 1

    def visitTerminal(self, node: TerminalNode):
        print(node)


class Python3ParserTests(TestCase):

    def setup(self, path):
        input = FileStream(path, encoding="utf-8")
        lexer = Python3Lexer(input)
        stream = CommonTokenStream(lexer)

        # print out the token parsing
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
            to_app = (type(actual_ast).__name__, actual_ast.name)
        else:
            to_app = type(actual_ast).__name__
        path.append(to_app)

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

        generated_tree = PyHoleVisitor().visit(tree)
        print(ast.dump(generated_tree, indent=1))

        with open("test/q1_3.py") as file:
            python_tree = ast.parse(file.read(), "test/q1_3.py")
            print()
            print(ast.dump(python_tree, indent=1))
            self.asts_equal(python_tree, generated_tree)

    def test_ast_generator_student2(self):
        parser = self.setup("test/q1_254.py")
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)
        print(ast.dump(generated_tree, indent=1))

        with open("test/q1_254.py") as file:
            python_tree = ast.parse(file.read(), "test/q1_254.py")
            print()
            print(ast.dump(python_tree, indent=1))
            self.asts_equal(python_tree, generated_tree)

    def test_ast_generator_complex(self):
        parser = self.setup("test/test_grammar.py")
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)
        print(ast.dump(generated_tree, indent=1))

        with open("test/test_grammar.py") as file:
            python_tree = ast.parse(file.read(), "test/test_grammar.py")
            print()
            print(ast.dump(python_tree, indent=1))
            self.asts_equal(python_tree, generated_tree)


class TestASTHole(TestCase):
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

    @pytest.mark.timeout(10)
    def test_ast_equal_match(self):
        val = match_files("test/q1_3.py", "test/q1_3.py")
        self.assertTrue(val)

        val = match_files("test/q1_254.py", "test/q1_254.py")
        self.assertTrue(val)

        val = match_files("test/q1_3.py", "test/q1_254.py")
        self.assertFalse(val)

        val = match_files("test/q1_254.py", "test/q1_3.py")
        self.assertFalse(val)

    @pytest.mark.timeout(10)
    def test_ast_simple_hole(self):
        parser = self.setup("test/pyHoleTest.py")
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        wrong_parser = self.setup("test/pyHoleNok.py")
        wrong_tree = wrong_parser.file_input()

        wrong_generated_tree = PyHoleVisitor().visit(wrong_tree)

        with open("test/q1_3.py") as file:
            python_tree = ast.parse(file.read(), "test/q1_3.py")
            val = Matcher().match(generated_tree, python_tree)
            self.assertTrue(val)

            wrong_val = Matcher().match(wrong_generated_tree, python_tree)
            self.assertFalse(wrong_val)

    @pytest.mark.timeout(10)
    def test_ast_compound_hole(self):
        parser_ok = self.setup("test/pyHoleCompoundOk.py")
        tree_ok = parser_ok.file_input()

        generated_tree_ok = PyHoleVisitor().visit(tree_ok)

        with open("test/q1_254.py") as file:
            python_tree = ast.parse(file.read(), "test/q1_254.py")

            val_ok = Matcher().match(generated_tree_ok, python_tree)
            self.assertTrue(val_ok)

    @pytest.mark.timeout(10)
    def test_ast_labeled_hole(self):
        val = match_files("test/pyHoleLabeled.py", "test/q1_3.py")
        self.assertTrue(val)

    @pytest.mark.timeout(10)
    def test_ast_multiple_depth(self):
        val = match_files("test/pyHoleMultipleDepth.py", "test/q1_254.py")
        self.assertTrue(val)
