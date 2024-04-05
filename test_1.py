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

def filter_file(input_filename, keyword, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
    
    keyword = keyword.lower()
    
    # Обираємо потрібні рядки
    filtered_lines = [line for line in lines if keyword in line.lower()]

    # Записуємо результат у новий файл
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.writelines(filtered_lines)

