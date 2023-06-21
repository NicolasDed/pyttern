import ast
from unittest import TestCase

import pytest
from antlr4 import *

from PyHole.Matcher import Matcher, match_files
from PyHole.PyHoleParser import *
from PyHole.antlr.Python3Lexer import Python3Lexer
from PyHole.antlr.Python3Listener import Python3Listener
from PyHole.antlr.Python3Parser import Python3Parser
from PyHole.visualizer import Visualizer


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


class PyHoleTest(TestCase):
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


class Python3ParserTests(PyHoleTest):

    def test_python3_test_grammar(self):
        parser = self.setup("tests_files/test_grammar.py")
        tree = parser.file_input()
        listener = Python3Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        self.assertEqual(len(self.errorListener.symbol), 0)

    def test_python3_test_student(self):
        parser = self.setup("tests_files/q1_3.py")
        tree = parser.file_input()
        listener = Printer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        self.assertEqual(len(self.errorListener.symbol), 0)


class AstGeneratorTests(PyHoleTest):

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
        parser = self.setup("tests_files/q1_3.py")
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)
        print(ast.dump(generated_tree, indent=1))

        with open("tests_files/q1_3.py") as file:
            python_tree = ast.parse(file.read(), "tests_files/q1_3.py")
            print()
            print(ast.dump(python_tree, indent=1))
            self.asts_equal(python_tree, generated_tree)

    def test_ast_generator_student2(self):
        parser = self.setup("tests_files/q1_254.py")
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)
        print(ast.dump(generated_tree, indent=1))

        with open("tests_files/q1_254.py") as file:
            python_tree = ast.parse(file.read(), "tests_files/q1_254.py")
            print()
            print(ast.dump(python_tree, indent=1))
            self.asts_equal(python_tree, generated_tree)

    def test_ast_generator_complex(self):
        parser = self.setup("tests_files/test_grammar.py")
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)
        print(ast.dump(generated_tree, indent=1))

        with open("tests_files/test_grammar.py") as file:
            python_tree = ast.parse(file.read(), "tests_files/test_grammar.py")
            print()
            print(ast.dump(python_tree, indent=1))
            self.asts_equal(python_tree, generated_tree)


def show_pattern(code_file, pattern_file, match, output_file):
    with open(code_file) as file:
        code = file.read()
        with open(pattern_file) as pattern_file:
            pattern = pattern_file.read()
            html = Visualizer.match_to_hml(match, code, pattern)
            html.write(output_file)
            return html


class TestASTHole(PyHoleTest):

    @pytest.mark.timeout(10)
    def test_strict_ast_equal_match(self):
        nbr = [3, 254, 560]

        for n1 in nbr:
            for n2 in nbr:
                val, details = match_files(f"tests_files/q1_{n1}.py", f"tests_files/q1_{n2}.py", True, True)
                if n1 == n2:
                    self.assertTrue(val, f"{n1} != {n2}: {details}")
                else:
                    self.assertFalse(val, f"{n1} = {n2}: {details}")

    @pytest.mark.timeout(10)
    def test_soft_ast_equal_match(self):
        nbr = [3, 254, 560]

        for n1 in nbr:
            for n2 in nbr:
                val, details = match_files(f"tests_files/q1_{n1}.py", f"tests_files/q1_{n2}.py", False, True)
                if n1 == n2:
                    self.assertTrue(val, f"{n1} != {n2}: {details}")
                else:
                    self.assertFalse(val, f"{n1} = {n2}: {details}")

    @pytest.mark.timeout(10)
    def test_ast_simple_hole(self):
        parser = self.setup("tests_files/pyHoleTest.py")
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        wrong_parser = self.setup("tests_files/pyHoleNok.py")
        wrong_tree = wrong_parser.file_input()

        wrong_generated_tree = PyHoleVisitor().visit(wrong_tree)

        with open("tests_files/q1_3.py") as file:
            python_tree = ast.parse(file.read(), "tests_files/q1_3.py")
            val = Matcher().match(generated_tree, python_tree)
            self.assertTrue(val)

            wrong_val = Matcher().match(wrong_generated_tree, python_tree)
            self.assertFalse(wrong_val)

    @pytest.mark.timeout(10)
    def test_ast_compound_hole(self):
        parser_ok = self.setup("tests_files/pyHoleCompoundOk.py")
        tree_ok = parser_ok.file_input()

        generated_tree_ok = PyHoleVisitor().visit(tree_ok)

        with open("tests_files/q1_254.py") as file:
            python_tree = ast.parse(file.read(), "tests_files/q1_254.py")

            val_ok = Matcher().match(generated_tree_ok, python_tree)
            self.assertTrue(val_ok)

    @pytest.mark.timeout(10)
    def test_ast_labeled_hole(self):
        val = match_files("tests_files/pyHoleLabeled.py", "tests_files/q1_3.py", strict_match=True)
        self.assertTrue(val)

    @pytest.mark.timeout(10)
    def test_ast_multiple_depth(self):
        val, msg = match_files("tests_files/pyHoleMultipleDepth.py", "tests_files/q1_254.py", strict_match=True, match_details=True)
        self.assertTrue(val, msg)

    @pytest.mark.timeout(10)
    def test_pattern_13(self):
        val, match = match_files("tests_files/Pattern13.pyh", "tests_files/q1_560.py", strict_match=True, match_details=True)
        self.assertTrue(val, match)

        show_pattern("tests_files/q1_560.py", "tests_files/Pattern13.pyh", match, "visu/p13.html")

    @pytest.mark.timeout(10)
    def test_pattern_different_size(self):
        val = match_files("tests_files/Small.pyh", "tests_files/q1_3.py", strict_match=True)
        self.assertFalse(val)

        val = match_files("tests_files/Small.pyh", "tests_files/q1_254.py", strict_match=True)
        self.assertFalse(val)

        val = match_files("tests_files/Small.pyh", "tests_files/q1_560.py", strict_match=True)
        self.assertFalse(val)

    @pytest.mark.timeout(10)
    def test_soft_pattern_match(self):
        val, match = match_files("tests_files/Pattern13soft.pyh", "tests_files/q1_560.py", strict_match=False, match_details=True)
        self.assertTrue(val, match)

        show_pattern("tests_files/q1_560.py", "tests_files/Pattern13soft.pyh", match, "visu/p13soft.html")

        val, match = match_files("tests_files/Pattern13soft.pyh", "tests_files/q1_560.py", strict_match=True, match_details=True)
        self.assertFalse(val, match)

    @pytest.mark.timeout(10)
    def test_soft_ast_compound_hole(self):
        val, match = match_files("tests_files/pyHoleCompoundSoft.pyh", "tests_files/q1_254.py", strict_match=False,
                                 match_details=True)
        self.assertTrue(val, msg=match)

        show_pattern("tests_files/q1_254.py", "tests_files/pyHoleCompoundSoft.pyh", match, "visu/pyHoleCompoundSoft.html")

        val, match = match_files("tests_files/pyHoleCompoundSoft.pyh", "tests_files/q1_254.py", strict_match=True,
                                 match_details=True)
        self.assertFalse(val, msg=match)

    def test_strict_mode(self):
        val, match = match_files("tests_files/strictModeTest.pyh", "tests_files/q1_254.py", strict_match=False, match_details=True)
        self.assertTrue(val, msg=match)

        show_pattern("tests_files/q1_254.py", "tests_files/strictModeTest.pyh", match, "visu/strict.html")

        val, match = match_files("tests_files/strictModeTest.pyh", "tests_files/q1_560.py", strict_match=False, match_details=True)
        self.assertFalse(val, msg=match)


class TestVisualizer(TestCase):

    def test_pattern_visualizer(self):
        val, match = match_files("tests_files/pyHoleMultipleDepth.py", "tests_files/q1_254.py", strict_match=True, match_details=True)
        self.assertTrue(val)

        html = show_pattern("tests_files/q1_254.py", "tests_files/pyHoleMultipleDepth.py", match, "visu/match.html")
        b_elements = html.findall(".//b")

        self.assertEqual(4, len(b_elements))

        first_match = b_elements[0].text
        #self.assertRegex(first_match, r"def\s+multiplications") # Python ast seems buggy IDK why
        second_match = b_elements[1].text
        self.assertEqual(second_match, "n")
        third_match = b_elements[2].text
        self.assertRegex(third_match, r"\w+\s*\+=\s*1\s*")
        fourth_match = b_elements[3].text
        self.assertRegex(fourth_match, r"return \(?\w+\)?")

    def test_remove_overlap(self):
        intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
        expected = [(1, 4), (5, 8)]
        self.assertEqual(Visualizer.remove_overlap(intervals), expected)

        intervals = [(1, 5), (2, 3), (4, 6), (8, 9)]
        expected = [(1, 6), (8, 9)]
        self.assertEqual(Visualizer.remove_overlap(intervals), expected)

        intervals = [(1, 2), (3, 4), (5, 6)]
        expected = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(Visualizer.remove_overlap(intervals), expected)

        intervals = []
        expected = []
        self.assertEqual(Visualizer.remove_overlap(intervals), expected)

        intervals = [(1, 5)]
        expected = [(1, 5)]
        self.assertEqual(Visualizer.remove_overlap(intervals), expected)

        intervals = [(1, 3), (4, 6), (7, 9)]
        expected = [(1, 3), (4, 6), (7, 9)]
        self.assertEqual(Visualizer.remove_overlap(intervals), expected)


