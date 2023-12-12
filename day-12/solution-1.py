from pathlib import Path
import os
from collections import Counter
from itertools import pairwise
import copy
import re

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

row_list = []
for index, line in enumerate(file_lines_list):
    text = line.split()[0]
    groups = [ int(i) for i in line.split()[1].split(",")]
    row_list.append((text, groups))

def get_lengths(input_string):
    pattern = re.compile("[?#]+")
    matches = pattern.findall(input_string)
    lengths = [len(match) for match in matches]
    return lengths

def get_number_of_arrangements(row):
    text: str = row[0]
    groups: list = row[1]
    lengths = get_lengths(text)
    print(text, "  ", groups, "  ", lengths)
    
    pass

result_list = []
for row in row_list:
    result_list.append(get_number_of_arrangements(row))


pass

