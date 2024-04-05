import pytest
import os
from code1 import filter_file

@pytest.fixture
def input_filename():
    return "file.txt"

@pytest.fixture
def output_filename():
    return "filtered.txt"

@pytest.fixture
def create_input_file(input_filename):
    with open(input_filename, 'w', encoding='utf-8') as file:
        file.write("This is a test file\n")
        file.write("Containing some lines with RUR\n")
        file.write("And some lines without it\n")

@pytest.fixture
def cleanup_files(input_filename, output_filename):
    yield
    os.remove(input_filename)
    os.remove(output_filename)

@pytest.mark.parametrize("keyword, expected_lines", [
    ("rur", ["Containing some lines with RUR\n"]),
    ("apple", [])
])
def test_filter_file(create_input_file, cleanup_files, input_filename, output_filename, keyword, expected_lines):
    filter_file(input_filename, keyword, output_filename)

    with open(output_filename, 'r', encoding='utf-8') as output_file:
        filtered_lines = output_file.readlines()

    assert filtered_lines == expected_lines
