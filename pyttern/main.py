import argparse
import glob
import io
from functools import cache

from antlr4 import FileStream, CommonTokenStream, InputStream
from loguru import logger
from tqdm import tqdm

from .PytternListener import ConsolePytternListener
from .antlr import Python3Parser
from .antlr.Python3Lexer import Python3Lexer
from .pyttern_error_listener import Python3ErrorListener
from .pytternfsm.python_visitor import Python_Visitor
from .pytternfsm.tree_pruner import TreePruner
from .simulator.simulator import Simulator


def match_files(pattern_path, code_path, strict_match=False, match_details=False):
    try:
        pattern = generate_tree_from_file(pattern_path)
        code = generate_tree_from_file(code_path)
    except Exception as e:
        assert False, e

    fsm = Python_Visitor(strict_match).visit(pattern)

    simu = Simulator(fsm, code)
    simu.start()
    while len(simu.states) > 0:
        simu.step()
    if match_details:
        return len(simu.match_set.matches) > 0, simu.match_set.matches
    return len(simu.match_set.matches) > 0


def match_wildcards(pattern_path, code_path, strict_match=False, match_details=False):
    """
    Match all python files with all pattern files.
    The path_pattern_with_wildcards and path_python_with_wildcard
    can contain wildcards. The function returns a dictionary with the results of the matches.
    :param pattern_path: Path to the pattern files with wildcards.
    :param code_path: Path to the python files with wildcards.
    :param strict_match: If True, the match will be strict, otherwise it will be soft.
    :param match_details: If True, the function will return the match details.
    :return: Dictionary with the results of the matches.
    """
    ret = {}
    patterns_filespath = glob.glob(str(pattern_path))
    pythons_filespath = glob.glob(str(code_path))

    try:
        pythons_filespath = tqdm(pythons_filespath)
    except NameError:
        pass

    for python_filepath in pythons_filespath:
        for pattern_filepath in patterns_filespath:
            result = match_files(pattern_filepath, python_filepath, strict_match, match_details)
            if python_filepath not in ret:
                ret[python_filepath] = {}
            ret[python_filepath][pattern_filepath] = result
    return ret


@cache
def generate_tree_from_code(code):
    code = code.strip() + "\n"
    stream = InputStream(code)
    return generate_tree_from_stream(stream)


@cache
def generate_tree_from_stream(stream):
    logger.info("Generating tree")
    lexer = Python3Lexer(stream)
    stream = CommonTokenStream(lexer)
    py_parser = Python3Parser(stream)

    error = io.StringIO()

    py_parser.removeErrorListeners()
    error_listener = Python3ErrorListener(error)
    py_parser.addErrorListener(error_listener)

    tree = py_parser.file_input()
    if len(error_listener.symbol) > 0:
        raise IOError(
            f"Syntax error in {stream} at line {error_listener.line} "
            f"({repr(error_listener.symbol)}) : {error.getvalue()}")

    pruned_tree = TreePruner().visit(tree)

    return pruned_tree


@cache
def generate_tree_from_file(file):
    file_input = FileStream(file, encoding="utf-8")
    return generate_tree_from_stream(file_input)


def run_application():
    from .visualizer.web import application
    application.app.run(debug=True)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--web", action="store_true")

    parser.add_argument("pattern")
    parser.add_argument("code")

    args = parser.parse_args()

    if args and args.web:
        run_application()
        return

    pattern = args.pattern
    code = args.code

    try:
        pattern_tree = generate_tree_from_file(pattern)
        code_tree = generate_tree_from_file(code)
    except Exception as e:
        print(e)
        return

    fsm = Python_Visitor().visit(pattern_tree)

    simu = Simulator(fsm, code_tree)

    listener = ConsolePytternListener()
    simu.add_listener(listener)
    simu.start()

    while len(simu.states) > 0:
        simu.step()
    print(simu.match_set.matches)

logger.disable("pyttern")
if __name__ == "__main__":
    logger.enable("pyttern")
    main()
