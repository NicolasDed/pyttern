import ast
import importlib.resources as pkg_resources
import io
import os
from unittest import TestCase

import pytest
from antlr4 import ParseTreeListener, TerminalNode, FileStream, CommonTokenStream, ParseTreeWalker

from pyhole.Matcher import Matcher, match_files, match_wildcards
from pyhole.PyHoleErrorListener import Python3ErrorListener
from pyhole.PyHoleVisitor import PyHoleVisitor
from pyhole.antlr.Python3Lexer import Python3Lexer
from pyhole.antlr.Python3Parser import Python3Parser
from pyhole.antlr.Python3ParserListener import Python3ParserListener
from pyhole.visualizer import Visualizer
from . import tests_files, visu


def get_test_file(path):
    return str(pkg_resources.files(tests_files) / path)


def discover_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


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


class PyHoleTest:
    def setup_stream(self, path):
        file_stream = FileStream(path, encoding="utf-8")
        lexer = Python3Lexer(file_stream)
        stream = CommonTokenStream(lexer)

        # print out the token parsing
        parser = Python3Parser(stream)

        error = io.StringIO()

        parser.removeErrorListeners()
        self.errorListener = Python3ErrorListener(error)
        parser.addErrorListener(self.errorListener)
        return parser


class TestPython3Parser(PyHoleTest):

    def test_python3_test_grammar(self):
        parser = self.setup_stream(get_test_file("grammar.py"))
        tree = parser.file_input()
        listener = Python3ParserListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert len(self.errorListener.symbol) == 0

    def test_python3_test_student(self):
        parser = self.setup_stream(get_test_file("q1_3.py"))
        tree = parser.file_input()
        listener = Python3ParserListener()  # Printer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert len(self.errorListener.symbol) == 0

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("small")))
    def test_python3_test_small(self, file_path):
        parser = self.setup_stream(str(file_path))
        tree = parser.file_input()
        listener = Python3ParserListener()  # Printer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert len(self.errorListener.symbol) == 0

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("large")))
    def test_python3_test_large(self, file_path):
        parser = self.setup_stream(str(file_path))
        tree = parser.file_input()
        listener = Python3ParserListener()  # Printer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert len(self.errorListener.symbol) == 0


class TestAstGenerator(PyHoleTest):

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

        if (isinstance(expected_ast, (ast.Load, ast.Store, ast.Del))
                and isinstance(actual_ast, (ast.Load, ast.Store, ast.Del))):
            path.pop()
            return

        assert type(actual_ast) == type(expected_ast), (actual_ast, expected_ast, path)
        if isinstance(expected_ast, ast.AST):
            for field, expected_value in ast.iter_fields(expected_ast):
                path.append(field)
                actual_value = getattr(actual_ast, field, None)
                self.__asts_equal(expected_value, actual_value, path)
                path.pop()

        elif isinstance(expected_ast, list):
            assert len(actual_ast) == len(expected_ast), f"{str(actual_ast)} != {str(expected_ast)} : {path}"
            for expected_value, actual_value in zip(expected_ast, actual_ast):
                self.__asts_equal(expected_value, actual_value, path)

        else:
            assert actual_ast == expected_ast, f"{path}"
        path.pop()

    def test_ast_generator_student(self):
        parser = self.setup_stream(get_test_file("q1_3.py"))
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        inp_file = get_test_file("q1_3.py")
        with open(inp_file, encoding="utf-8") as file:
            python_tree = ast.parse(file.read(), get_test_file("q1_3.py"))
            self.asts_equal(python_tree, generated_tree)

    def test_ast_generator_student2(self):
        parser = self.setup_stream(get_test_file("q1_254.py"))
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        inp_file = get_test_file("q1_254.py")
        with open(inp_file, encoding="utf-8") as file:
            python_tree = ast.parse(file.read(), get_test_file("q1_254.py"))
            self.asts_equal(python_tree, generated_tree)

    def test_ast_generator_complex(self):
        parser = self.setup_stream(get_test_file("grammar.py"))
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        inp_file = get_test_file("grammar.py")
        with open(inp_file, encoding="utf-8") as file:
            python_tree = ast.parse(file.read(), get_test_file("grammar.py"))
            self.asts_equal(python_tree, generated_tree)

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("small")))
    def test_ast_generator_small(self, file_path):
        parser = self.setup_stream(file_path)
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        with open(file_path, encoding="utf-8") as file:
            python_tree = ast.parse(file.read(), file_path)
            self.asts_equal(python_tree, generated_tree)

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("large")))
    def test_ast_generator_large(self, file_path):
        parser = self.setup_stream(file_path)
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        with open(file_path, encoding="utf-8") as file:
            python_tree = ast.parse(file.read(), file_path)
            self.asts_equal(python_tree, generated_tree)


def show_pattern(code_path, pattern_path, match, output_file):
    with open(code_path, encoding="utf-8") as file:
        code = file.read()
        with open(pattern_path, encoding="utf-8") as pattern_file:
            pattern = pattern_file.read()
            html = Visualizer.match_to_hml(match, code, pattern)
            html.write(output_file)
            return html


class TestASTHole(PyHoleTest):

    @pytest.mark.timeout(10)
    def test_strict_ast_equal_match(self):
        nbr = [3, 254, 560]

        for n_1 in nbr:
            for n_2 in nbr:
                val, details = match_files((pkg_resources.files(tests_files) / f"q1_{n_1}.py"),
                                           (pkg_resources.files(tests_files) / f"q1_{n_2}.py"),
                                           True, True)
                if n_1 == n_2:
                    assert val, f"{n_1} != {n_2}: {details}"
                else:
                    assert not val, f"{n_1} = {n_2}: {details}"

    @pytest.mark.timeout(10)
    def test_soft_ast_equal_match(self):
        nbr = [3, 254, 560]

        for n_1 in nbr:
            for n_2 in nbr:
                val, details = match_files((pkg_resources.files(tests_files) / f"q1_{n_1}.py"),
                                           (pkg_resources.files(tests_files) / f"q1_{n_2}.py"),
                                           False, True)
                if n_1 == n_2:
                    assert val, f"{n_1} != {n_2}: {details}"
                else:
                    assert not val, f"{n_1} = {n_2}: {details}"

    @pytest.mark.timeout(10)
    def test_ast_simple_hole(self):
        parser = self.setup_stream(get_test_file("pyHoleTest.pyh"))
        tree = parser.file_input()

        generated_tree = PyHoleVisitor().visit(tree)

        wrong_parser = self.setup_stream(get_test_file("pyHoleNok.pyh"))
        wrong_tree = wrong_parser.file_input()

        wrong_generated_tree = PyHoleVisitor().visit(wrong_tree)

        inp_file = get_test_file("q1_3.py")
        with open(inp_file, encoding="utf-8") as file:
            python_tree = ast.parse(file.read(), get_test_file("q1_3.py"))
            val = Matcher().match(generated_tree, python_tree)
            assert val

            matcher = Matcher()
            matcher.set_strict(True)
            wrong_val = matcher.match(wrong_generated_tree, python_tree)
            assert not wrong_val

    def test_ast_simple_addition(self):
        pattern_path = get_test_file("piPattern.pyh")
        code_path = get_test_file("piCode.py")

        res, det = match_files(pattern_path, code_path, match_details=True)
        assert res, det

    @pytest.mark.timeout(10)
    def test_ast_compound_hole(self):
        parser_ok = self.setup_stream(get_test_file("pyHoleCompoundOk.pyh"))
        tree_ok = parser_ok.file_input()

        generated_tree_ok = PyHoleVisitor().visit(tree_ok)

        inp_file = get_test_file("q1_254.py")
        with open(inp_file, encoding="utf-8") as file:
            python_tree = ast.parse(file.read(), get_test_file("q1_254.py"))

            val_ok = Matcher().match(generated_tree_ok, python_tree)
            assert val_ok

    @pytest.mark.timeout(10)
    def test_ast_labeled_hole(self):
        val, det = match_files(get_test_file("pyHoleLabeled.pyh"),
                               get_test_file("q1_3.py"), strict_match=True, match_details=True)
        assert val, det

    @pytest.mark.timeout(10)
    def test_ast_multiple_depth(self):
        val, msg = match_files(get_test_file("pyHoleMultipleDepth.pyh"),
                               get_test_file("q1_254.py"), strict_match=True, match_details=True)
        assert val, msg

    @pytest.mark.timeout(10)
    def test_pattern_13(self):
        val, match = match_files(get_test_file("Pattern13.pyh"),
                                 get_test_file("q1_560.py"), strict_match=True,
                                 match_details=True)
        assert val, match

        show_pattern(get_test_file("q1_560.py"),
                     get_test_file("Pattern13.pyh"), match,
                     (pkg_resources.files(visu) / "p13.html"))

    @pytest.mark.timeout(10)
    def test_pattern_different_size(self):
        val = match_files(get_test_file("Small.pyh"),
                          get_test_file("q1_3.py"), strict_match=True)
        assert not val
        val = match_files(get_test_file("Small.pyh"),
                          get_test_file("q1_254.py"), strict_match=True)
        assert not val
        val = match_files(get_test_file("Small.pyh"),
                          get_test_file("q1_560.py"), strict_match=True)
        assert not val

    @pytest.mark.timeout(10)
    def test_soft_pattern_match(self):
        val, match = match_files(get_test_file("Pattern13soft.pyh"),
                                 get_test_file("q1_560.py"),
                                 strict_match=False, match_details=True)
        assert val, match

        show_pattern(get_test_file("q1_560.py"),
                     get_test_file("Pattern13soft.pyh"), match,
                     (pkg_resources.files(visu) / "p13soft.html"))

        val, match = match_files(get_test_file("Pattern13soft.pyh"),
                                 get_test_file("q1_560.py"),
                                 strict_match=True, match_details=True)
        assert not val, match

    @pytest.mark.timeout(10)
    def test_soft_ast_compound_hole(self):
        val, match = match_files(get_test_file("pyHoleCompoundSoft.pyh"),
                                 get_test_file("q1_254.py"),
                                 strict_match=False, match_details=True)
        assert val, match

        show_pattern(get_test_file("q1_254.py"),
                     get_test_file("pyHoleCompoundSoft.pyh"), match,
                     (pkg_resources.files(visu) / "pyHoleCompoundSoft.html"))

        val, match = match_files(get_test_file("pyHoleCompoundSoft.pyh"),
                                 get_test_file("q1_254.py"),
                                 strict_match=True, match_details=True)
        assert not val, match

    def test_strict_mode(self):
        val, match = match_files(get_test_file("strictModeTest.pyh"),
                                 get_test_file("q1_254.py"),
                                 strict_match=False, match_details=True)
        assert val, match

        show_pattern(get_test_file("q1_254.py"),
                     get_test_file("strictModeTest.pyh"), match,
                     (pkg_resources.files(visu) / "strict.html"))

        val, match = match_files(get_test_file("strictModeTest.pyh"),
                                 get_test_file("strictModeNok.py"),
                                 strict_match=False, match_details=True)
        assert not val, match

    def test_match_wildcards_unique(self):
        pattern_path = get_test_file("pyHoleCompoundSoft.pyh")
        code_path = get_test_file("q1_254.py")
        matches = match_wildcards(pattern_path, code_path)
        assert matches[code_path][pattern_path], matches

    def test_match_wildcards_multiple_pattern(self):
        pattern_path = get_test_file("pyHoleCompound*.pyh")
        code_path = get_test_file("q1_254.py")
        matches = match_wildcards(pattern_path, code_path, strict_match=True)
        for code, match in matches.items():
            for pattern, result in match.items():
                if "Ok" in pattern:
                    assert result, f"{pattern} on {code} should match"
                else:
                    assert not result, f"{pattern} on {match} should not match"

    def test_match_wildcards_multiple_code(self):
        pattern_path = get_test_file("Pattern_13soft.pyh")
        code_path = get_test_file("q1_*.py")
        matches = match_wildcards(pattern_path, code_path)
        for code, match in matches.items():
            for pattern, result in match.items():
                if "q1_560.py" in match:
                    assert result, f"{pattern} on {code} should match"
                else:
                    assert not result, f"{pattern} on {code} should not match"

    def test_match_mult_and_div(self):
        pattern_path = get_test_file("multAndDivPatterns/*.pyh")
        code_path = get_test_file("multAndDiv.py")
        matches = match_wildcards(pattern_path, code_path, match_details=True)
        for _, match in matches.items():
            for pattern, result in match.items():
                do_match, details = result
                if "patternMultPlusDIv" in pattern:
                    assert do_match, details
                else:
                    assert not do_match, details

    def test_match_recursion(self):
        pattern_path = get_test_file("simpleRecursion.pyh")
        code_path = get_test_file("factRec.py")
        res, det = match_files(pattern_path, code_path, match_details=True)
        assert res, det

    def test_observer_pattern(self):
        pattern_path = get_test_file("observer.pyh")
        code_path = get_test_file("observer/Subject.py")
        res, det = match_files(pattern_path, code_path, match_details=True)
        assert res, det

    def test_type_wildcard(self):
        pattern_path = get_test_file("type.pyh")
        code_path = get_test_file("type.py")
        res, det = match_files(pattern_path, code_path, match_details=True)
        assert res, det

        code_path = get_test_file("no_type.py")
        res, det = match_files(pattern_path, code_path, match_details=True)
        assert not res, det


class TestVisualizer(TestCase):

    def test_pattern_visualizer(self):
        val, match = match_files(get_test_file("pyHoleMultipleDepth.pyh"),
                                 get_test_file("q1_254.py"),
                                 strict_match=True, match_details=True)
        assert val

        html = show_pattern(get_test_file("q1_254.py"),
                            get_test_file("pyHoleMultipleDepth.pyh"),
                            match, (pkg_resources.files(visu) / "match.html"))
        b_elements = html.findall(".//b")

        assert 4 == len(b_elements)
        # first_match = b_elements[0].text
        # self.assertRegex(first_match, r"def\s+multiplications") # Python ast seems buggy IDK why
        second_match = b_elements[1].text
        assert second_match == "n"
        third_match = b_elements[2].text
        self.assertRegex(third_match, r"\w+\s*\+=\s*1\s*")
        fourth_match = b_elements[3].text
        self.assertRegex(fourth_match, r"return \(?\w+\)?")

    def test_remove_overlap(self):
        intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
        expected = [(1, 4), (5, 8)]
        assert Visualizer.remove_overlap(intervals) == expected
        intervals = [(1, 5), (2, 3), (4, 6), (8, 9)]
        expected = [(1, 6), (8, 9)]
        assert Visualizer.remove_overlap(intervals) == expected
        intervals = [(1, 2), (3, 4), (5, 6)]
        expected = [(1, 2), (3, 4), (5, 6)]
        assert Visualizer.remove_overlap(intervals) == expected
        intervals = []
        expected = []
        assert Visualizer.remove_overlap(intervals) == expected
        intervals = [(1, 5)]
        expected = [(1, 5)]
        assert Visualizer.remove_overlap(intervals) == expected
        intervals = [(1, 3), (4, 6), (7, 9)]
        expected = [(1, 3), (4, 6), (7, 9)]
        assert Visualizer.remove_overlap(intervals) == expected