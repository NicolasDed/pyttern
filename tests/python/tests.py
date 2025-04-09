import importlib.resources as pkg_resources
import os
import time

import pytest
from loguru import logger

from pyttern.matcher import match_files, match_wildcards
from tests.python import tests_files


def get_test_file(path):
    return str(pkg_resources.files(tests_files) / path)


def discover_files(directory, extension=None):
    for root, _, files in os.walk(directory):
        for file in files:
            if ".pyc" not in file:
                if extension is None or file.endswith(extension):
                    yield os.path.join(root, file)


class TestASTWildcards:

    LANGUAGE = "python"

    @pytest.mark.timeout(10)
    def test_strict_ast_equal_match(self):
        nbr = [3, 254, 560]

        for n_1 in nbr:
            for n_2 in nbr:
                val, details = match_files(
                    (pkg_resources.files(tests_files) / f"q1_{n_1}.py"),
                    (pkg_resources.files(tests_files) / f"q1_{n_2}.py"),
                    self.LANGUAGE, True, True
                )
                if n_1 == n_2:
                    assert val, f"{n_1} != {n_2}: {details}"
                else:
                    assert not val, f"{n_1} = {n_2}: {details}"

    @pytest.mark.timeout(10)
    def test_soft_ast_equal_match(self):
        nbr = [3, 254, 560]

        for n_1 in nbr:
            for n_2 in nbr:
                val, details = match_files(
                    (pkg_resources.files(tests_files) / f"q1_{n_1}.py"),
                    (pkg_resources.files(tests_files) / f"q1_{n_2}.py"),
                    self.LANGUAGE, False, True
                )
                if n_1 == n_2:
                    assert val, f"{n_1} != {n_2}: {details}"
                else:
                    assert not val, f"{n_1} = {n_2}: {details}"

    @pytest.mark.timeout(10)
    def test_ast_simple_wildcard(self):
        pattern_path = get_test_file("pytternTest.pyh")
        code_path = get_test_file("q1_3.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert res, det

        pattern_path = get_test_file("pytternNok.pyh")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert not res, det

    def test_ast_simple_addition(self):
        pattern_path = get_test_file("piPattern.pyh")
        code_path = get_test_file("piCode.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        assert res, det

    @pytest.mark.timeout(10)
    def test_ast_body_wildcard(self):
        pattern_path = get_test_file("pytternCompoundOk.pyh")
        code_path = get_test_file("q1_254.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert res, det

    @pytest.mark.timeout(10)
    def test_ast_labeled_wildcard(self):
        val, det = match_files(
            get_test_file("pytternLabeled.pyh"),
            get_test_file("q1_3.py"), self.LANGUAGE, strict_match=True, match_details=True
        )
        assert val, det

    @pytest.mark.timeout(10)
    def test_ast_multiple_depth(self):
        val, msg = match_files(
            get_test_file("pytternMultipleDepth.pyh"),
            get_test_file("q1_254.py"),
            self.LANGUAGE,strict_match=True, match_details=True
        )
        assert val, msg

    @pytest.mark.timeout(10)
    def test_pattern_13(self):
        val, match = match_files(
            get_test_file("Pattern13.pyh"),
            get_test_file("q1_560.py"),
            self.LANGUAGE, strict_match=True, match_details=True
        )
        assert val, match

    @pytest.mark.timeout(10)
    def test_pattern_different_size(self):
        val = match_files(get_test_file("Small.pyh"), get_test_file("q1_3.py"), self.LANGUAGE, strict_match=True)
        assert not val
        val = match_files(get_test_file("Small.pyh"), get_test_file("q1_254.py"), self.LANGUAGE, strict_match=True)
        assert not val
        val = match_files(get_test_file("Small.pyh"), get_test_file("q1_560.py"), self.LANGUAGE, strict_match=True)
        assert not val

    @pytest.mark.timeout(10)
    def test_soft_pattern_match(self):
        val, match = match_files(
            get_test_file("Pattern13soft.pyh"),
            get_test_file("q1_560.py"),
            self.LANGUAGE, strict_match=False, match_details=True
        )
        assert val, match

        val, match = match_files(
            get_test_file("Pattern13soft.pyh"),
            get_test_file("q1_560.py"),
            self.LANGUAGE, strict_match=True, match_details=True
        )
        assert not val, match

    @pytest.mark.timeout(10)
    def test_soft_ast_body_wildcard(self):
        val, match = match_files(
            get_test_file("pytternCompoundSoft.pyh"),
            get_test_file("q1_254.py"),
            self.LANGUAGE,strict_match=False, match_details=True
        )
        assert val, match

        val, match = match_files(
            get_test_file("pytternCompoundSoft.pyh"),
            get_test_file("q1_254.py"),
            self.LANGUAGE,strict_match=True, match_details=True
        )
        assert not val, match

    def test_strict_mode(self):
        val, match = match_files(
            get_test_file("strictModeTest.pyh"),
            get_test_file("q1_254.py"),
            self.LANGUAGE, strict_match=False, match_details=True
        )
        assert val, match

        val, match = match_files(
            get_test_file("strictModeTest.pyh"),
            get_test_file("strictModeNok.py"),
            self.LANGUAGE, strict_match=False, match_details=True
        )
        assert not val, match

    def test_match_wildcards_unique(self):
        pattern_path = get_test_file("pytternCompoundSoft.pyh")
        code_path = get_test_file("q1_254.py")
        matches = match_wildcards(pattern_path, code_path, self.LANGUAGE, strict_match=False)
        assert matches[code_path][pattern_path], matches

    def test_match_wildcards_multiple_pattern(self):
        pattern_path = get_test_file("pytternCompound*.pyh")
        code_path = get_test_file("q1_254.py")
        matches = match_wildcards(pattern_path, code_path, self.LANGUAGE, strict_match=True)
        for code, match in matches.items():
            for pattern, result in match.items():
                if "Ok" in pattern:
                    assert result, f"{pattern} on {code} should match"
                else:
                    assert not result, f"{pattern} on {match} should not match"

    def test_match_wildcards_multiple_code(self):
        pattern_path = get_test_file("Pattern_13soft.pyh")
        code_path = get_test_file("q1_*.py")
        matches = match_wildcards(pattern_path, code_path, self.LANGUAGE)
        for code, match in matches.items():
            for pattern, result in match.items():
                if "q1_560.py" in match:
                    assert result, f"{pattern} on {code} should match"
                else:
                    assert not result, f"{pattern} on {code} should not match"

    def test_match_mult_and_div(self):
        pattern_path = get_test_file("multAndDivPatterns/*.pyh")
        code_path = get_test_file("multAndDiv.py")
        matches = match_wildcards(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        for _, match in matches.items():
            for pattern, result in match.items():
                do_match, details = result
                if "patternMultPlusDIv" in pattern:
                    assert do_match, f"Cannot match {pattern}: {details}"
                else:
                    assert not do_match, details

    def test_match_recursion(self):
        pattern_path = get_test_file("simpleRecursion.pyh")
        code_path = get_test_file("factRec.py")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        assert res, det

    def test_observer_pattern(self):
        pattern_path = get_test_file("observer.pyh")
        code_path = get_test_file("observer/Subject.py")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        assert res, det

    def test_type_wildcard(self):
        pattern_path = get_test_file("type.pyh")
        code_path = get_test_file("type.py")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        assert res, det

        code_path = get_test_file("no_type.py")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert not res, det

    def test_augassign(self):
        pytest.skip("Not implemented")

        pattern_path = get_test_file("augassign.pyh")
        code_path = get_test_file("piCode.py")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert res, det

        code_path = get_test_file("piCodeBis.py")
        ret, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert ret, det

        pattern_path = get_test_file("augassignNok.pyh")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert not res, str(det)

        code_path = get_test_file("piCode.py")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert not res, str(det)

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("numbers")))
    def test_number_wildcard(self, file_path):
        pattern_path = get_test_file(file_path)
        code_path = get_test_file("type.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        if "Ok" in file_path:
            assert res, det
        elif "Ko" in file_path:
            assert not res, det
        else:
            assert False, f"Not ok nor ko in file name: {file_path}"

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("bodyNumbers")))
    def test_number_body_wildcard(self, file_path):
        pattern_path = get_test_file(file_path)
        code_path = get_test_file("strictModeNok.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        if "Ok" in file_path:
            assert res, det
        elif "Ko" in file_path:
            assert not res, det
        else:
            assert False, f"Not ok nor ko in file name: {file_path}"

    def test_nathan(self):
        pattern_path = get_test_file("nathan/pattern.pyh")
        code_path = get_test_file("nathan/code.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=True)
        assert not res, det

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("test_zero")))
    def test_zero_wildcard(self, file_path):
        pytest.skip("Not implemented")
        pattern_path = get_test_file(file_path)
        code_path = get_test_file("type.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        if "Ok" in file_path:
            assert res, det
        elif "Ko" in file_path:
            assert not res, det
        else:
            assert False, f"Not ok nor ko in file name: {file_path}"

    @pytest.mark.parametrize("file_path", discover_files(get_test_file("contains"), ".pyh"))
    @pytest.mark.parametrize("code_path", discover_files(get_test_file("contains"), ".py"))
    def test_contains_wildcard(self, file_path, code_path):
        pattern_path = get_test_file(file_path)
        code_path = get_test_file(code_path)

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        if "Ok" in file_path:
            assert res, det
        elif "Ko" in file_path:
            assert not res, det
        else:
            assert False, f"Not ok nor ko in file name: {file_path}"

    def test_too_much_indentation(self):
        pattern_path = get_test_file("toomuchindentation.pyt")
        code_path = get_test_file("q1_560.py")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        assert res, det

    def test_var_wildcard_in_arg(self):
        pattern_path = get_test_file("overwritten_arg/overwritten_arg.pyt")
        code_path = get_test_file("overwritten_arg/arg_*.py")

        matches = match_wildcards(pattern_path, code_path, self.LANGUAGE)

        for code, match in matches.items():
            for pattern, result in match.items():
                if "nok" in code:
                    assert not result, f"{pattern} on {code} should not match"
                else:
                    assert result, f"{pattern} on {code} should match"

    def test_missplaced_return(self):
        pattern_path = get_test_file("missplacedreturn/toplevelreturn.pyt")
        code_path = get_test_file("missplacedreturn/code55.py")

        # res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        # assert not res, det

        pattern_path = get_test_file("missplacedreturn/indentreturn.pyt")
        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
        assert res, det

    @pytest.mark.timeout(90)
    def test_big_load(self):
        logger.level("WARNING")
        start_time = time.time()
        pattern_path = get_test_file("multAndDivPatterns/*.pyh")
        code_path = get_test_file("multAndDiv.py")
        for _ in range(2000):
            matches = match_wildcards(pattern_path, code_path, self.LANGUAGE, match_details=True, strict_match=False)
            for _, match in matches.items():
                for pattern, result in match.items():
                    do_match, details = result
                    if "patternMultPlusDIv" in pattern:
                        assert do_match, f"Cannot match {pattern}: {details}"
                    else:
                        assert not do_match, details
        end_time = time.time()
        logger.level("INFO")
        assert end_time - start_time < 60, f"Execution took {end_time - start_time} seconds"
