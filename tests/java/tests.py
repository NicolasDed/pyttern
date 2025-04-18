import importlib.resources as pkg_resources
import os

import pytest
from loguru import logger

from pyttern.matcher import match_files, match_wildcards
from tests.java import tests_files


def get_test_file(path):
    return str(pkg_resources.files(tests_files) / path)


def discover_files(directory, extension=None):
    for root, _, files in os.walk(directory):
        for file in files:
            if ".class" not in file:
                if extension is None or file.endswith(extension):
                    yield os.path.join(root, file)


class TestASTWildcards:

    LANGUAGE = "java"

    @pytest.mark.timeout(10)
    def test_ast_equal_match(self):
        for n_1 in range(1, 3):
            for n_2 in range(1, 3):
                print(n_1, "-", n_2)
                pattern_path = get_test_file(f"ast_equal_match/t1_{n_1}.java")
                code_path = get_test_file(f"ast_equal_match/t1_{n_2}.java")

                val, details = match_files(pattern_path, code_path, self.LANGUAGE, False, True)

                logger.debug(f"Comparing t1_{n_1}.java with t1_{n_2}.java")
                if n_1 == n_2:
                    assert val, f"{n_1} != {n_2}: {details}"
                else:
                    assert not val, f"{n_1} = {n_2}: {details}"

    @pytest.mark.timeout(10)
    def test_simple_wildcard(self):
        pattern_path = get_test_file("simple_wildcard/ClassMainMethod.jat")
        code_path = get_test_file("simple_wildcard/ClassMainMethod.java")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert res, det

    @pytest.mark.timeout(10)
    def test_primitive_types(self):
        pattern_path = get_test_file("primitive_types/VariableName.jat")
        code_path = get_test_file("primitive_types/VariableName.java")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert res, det

    @pytest.mark.timeout(10)
    def test_list_wildcard(self):
        pattern_path = get_test_file("list_wildcard/ListWildcard.jat")
        code_path = get_test_file("list_wildcard/ListWildcard.java")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert res, det

    @pytest.mark.timeout(10)
    def test_simple_compound_wildcard(self):
        pattern_path = get_test_file("simple_compound_wildcard/SimpleCompoundWildcard.jat")
        code_path = get_test_file("simple_compound_wildcard/SimpleCompoundWildcard.java")

        res, det = match_files(pattern_path, code_path, self.LANGUAGE, match_details=True)
        assert res, det

    @pytest.mark.timeout(10)
    def test_var_wildcard(self):
        print("Testing matching var wildcards")
        for n in range(1, 4):
            pattern_path = get_test_file(f"var_wildcard/VarWildcard{n}.jat")
            code_path = get_test_file(f"var_wildcard/VarWildcard{n}.java")

            val, details = match_files(pattern_path, code_path, self.LANGUAGE, False, True)

            assert val, details

        print("Testing not matching var wildcards")
        for n in range(1, 2):
            pattern_path = get_test_file(f"var_wildcard/VarWildcard{n}Fail.jat")
            code_path = get_test_file(f"var_wildcard/VarWildcard{n}.java")

            val, details = match_files(pattern_path, code_path, self.LANGUAGE, False, True)

            assert not val, details