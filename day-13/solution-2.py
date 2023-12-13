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

maps_list = []
runner_idx = 0
empty_idx = 0
for index, line in enumerate(file_lines_list):
    if line == "" and empty_idx !=0:
        maps_list.append(file_lines_list[runner_idx+1:index])
        runner_idx = index
    if line == "" and empty_idx == 0:
        empty_idx += 1
        maps_list.append(file_lines_list[runner_idx:index])
        runner_idx = index
    if index == len(file_lines_list)-1:
        maps_list.append(file_lines_list[runner_idx+1:index+1])
        runner_idx = index

for index, matrix in enumerate(maps_list):
    maps_list[index] = [[matrix[h][w] for w in range(len(matrix[0]))] for h in range(len(matrix))]
    #maps_list[index] = zip(*maps_list[index])

def diff_no(r1: list, r2: list) -> int:
    diff = 0
    for element in zip(r1, r2):
        if element[0] != element[1]:
            diff += 1
    return diff

#print(diff_no([1, 1], [1, 2]))
#print(diff_no([1, 1], [1, 1]))

def is_a_perfect_reflection(line_idx, matrix, remaining_diff):
    remaining = remaining_diff
    r1 = list(range(line_idx, -1, -1))
    r2 = list(range(line_idx+1, len(matrix)))
    indeces = list(zip(r1, r2))
    for lin in indeces:
        print(lin)
        if matrix[lin[0]] != matrix[lin[1]] and remaining != 0:
            remaining = 0
            continue
        if matrix[lin[0]] != matrix[lin[1]] and remaining == 0:
            return False
    return True

result_dict = []
for index, matrix in enumerate(maps_list):
    print(f"**************")
    print(f"Matrix {index}")
    for i1, line_pair in enumerate(pairwise(matrix)):
        if diff_no(line_pair[0], line_pair[1]) == 0:
            print(f"Line pair found index: {i1+1}")
            print(f"{line_pair[0]}")
            print(f"{line_pair[1]}")
            if is_a_perfect_reflection(i1, matrix, 1):
                result_dict.append((i1+1)*100)
                print("It is a perfect reflection!")
                break
            else:
                print("It is NOT a perfect reflection!")
        if diff_no(line_pair[0], line_pair[1]) == 1:
            print(f"Line pair found index: {i1+1}")
            print(f"{line_pair[0]}")
            print(f"{line_pair[1]}")
            if is_a_perfect_reflection(i1, matrix, 0):
                result_dict.append((i1+1)*100)
                print("It is a perfect reflection!")
                break
            else:
                print("It is NOT a perfect reflection!")

    transposed = list(zip(*matrix))
    for i2, col_pair in enumerate(pairwise(transposed)):
        if diff_no(col_pair[0], col_pair[1]) == 0:
            print(f"Column pair found index: {i2+1}")
            print(f"{col_pair[0]}")
            print(f"{col_pair[1]}")
            if is_a_perfect_reflection(i2, transposed, 1):
                result_dict.append((i2+1))
                print("It is a perfect reflection!")
                break
            else:
                print("It is NOT a perfect reflection!")
        if diff_no(col_pair[0], col_pair[1]) == 1:
            print(f"Column pair found index: {i2+1}")
            print(f"{col_pair[0]}")
            print(f"{col_pair[1]}")
            if is_a_perfect_reflection(i2, transposed, 0):
                result_dict.append((i2+1))
                print("It is a perfect reflection!")
                break
            else:
                print("It is NOT a perfect reflection!")

print(sum(result_dict))
pass
