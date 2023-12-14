from pathlib import Path
import os
from collections import Counter
from itertools import pairwise
import copy
import re
import os
import numpy as np
import hashlib

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

char_2d_array = [[i for i in line] for line in file_lines_list]
char_2d_array = np.char.asarray(char_2d_array)


def move_round_rock_down_as_possible(line_idx, char_idx):
    cur_line_idx = line_idx
    if len(char_2d_array) > cur_line_idx >= 1:
        while char_2d_array[cur_line_idx-1][char_idx] == "." and cur_line_idx >= 1:
            char_2d_array[cur_line_idx-1][char_idx] = "O"
            char_2d_array[cur_line_idx][char_idx] = "."
            cur_line_idx -= 1

def print_array():
    os.system("cls")
    for line in char_2d_array:
        print("".join(line))

range_len = 1000000000
values_dict = {}
i = 0
while i < range_len:
    for i2 in range(4):
        for index_l, line in enumerate(char_2d_array):
            for index_c, char in enumerate(line):
                if char == "O":
                    move_round_rock_down_as_possible(index_l, index_c)
        char_2d_array = np.rot90(char_2d_array, 3)
        #print_array()
    serialized = char_2d_array.tobytes()
    hashed_key = hashlib.md5(serialized).hexdigest()
    if hashed_key in values_dict.keys():
        repeat_start = list(values_dict.keys()).index(hashed_key)
        repeat_end = i
        repeat_len = repeat_end-repeat_start
        to_add =  int((range_len-i)/repeat_len)
        i += to_add * repeat_len
    else:
        values_dict.update({hashed_key: i})
    i += 1


height = len(char_2d_array)
result_list = []
for index_l, line in enumerate(char_2d_array):
    for index_c, char in enumerate(line):
        if char == "O":
            result_list.append(height-index_l)
print(sum(result_list))
pass