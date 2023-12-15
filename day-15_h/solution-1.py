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


def calc_hash(string: str):
    cur_val = 0
    for char in string:
        cur_val = cur_val + ord(char)
        cur_val = cur_val * 17
        cur_val = int(cur_val % 256)
    return cur_val

res_list = []
split_list = [i for i in file_lines_list[0].split(",")]

for val in split_list:
    res_list.append(calc_hash(val))

print(sum(res_list))
pass