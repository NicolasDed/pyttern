import glob
from tqdm import tqdm

from pyttern.pytternfsm.python.python_visitor import Python_Visitor
from pyttern.simulator.simulator import Simulator
from .language_processors import get_processor


def match_files(pattern_path, code_path, language:str, strict_match=False, match_details=False):
    try:
        processor = get_processor(language)
        with open(pattern_path) as f:
            pyttern_code = f.read()
        with open(code_path) as f:
            code = f.read()

        pyttern_tree = processor.generate_tree_from_code(pyttern_code)
        pyttern_fsm = processor.create_fsm(pyttern_tree)
        code_tree = processor.generate_tree_from_code(code)
        simu = processor.create_simulator(pyttern_fsm, code_tree)
    except Exception as e:
        assert False, e

    simu.start()
    while len(simu.states) > 0:
        simu.step()
    print(f"Number of steps: {simu.n_step}")
    if match_details:
        return len(simu.match_set.matches) > 0, simu.match_set.matches
    return len(simu.match_set.matches) > 0


def match_wildcards(pattern_path, code_path, language:str, strict_match=False, match_details=False):
    """
    Match all python files with all pattern files.
    The path_pattern_with_wildcards and path_python_with_wildcard
    can contain wildcards. The function returns a dictionary with the results of the matches.
    :param pattern_path: Path to the pattern files with wildcards.
    :param code_path: Path to the python files with wildcards.
    :param language: programming language to use.
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
            result = match_files(pattern_filepath, python_filepath, language, strict_match, match_details)
            if python_filepath not in ret:
                ret[python_filepath] = {}
            ret[python_filepath][pattern_filepath] = result
    return ret