from pathlib import Path
import os
from collections import Counter
from itertools import pairwise, zip_longest
import copy
import re
from matplotlib import pyplot as plt

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

# x, y
dir_dict = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}

rows = []
for index, line in enumerate(file_lines_list):
    dir = line.split()[0]
    dir_len = int(line.split()[1])
    color = line.split()[2][1:-1]
    rows.append((dir, dir_len, color))

max_x = 0
max_y = 0
min_x = 0
min_y = 0

cur_x = 0
cur_y = 0
coords = []
coords.append((cur_x, cur_y))
for index, line in enumerate(rows):
    for cycle in range(line[1]):
        cur_x += dir_dict[line[0]][0]
        cur_y += dir_dict[line[0]][1]
        coords.append((cur_x, cur_y))
        max_x = max(max_x, cur_x)
        max_y = max(max_y, cur_y)
        min_x = min(min_x, cur_x)
        min_y = min(min_y, cur_y)

for i, coord in enumerate(coords):
    coords[i] = (coords[i][0], coords[i][1])

coords_set = set(coords)

#matrix = [["." for x in range(max_x+1)] for y in range(max_y+1)]
#width = len(matrix[0])
#height = len(matrix)

#for index, coord in enumerate(coords):
    #matrix[coord[1]][coord[0]] = "#"

def check_if_inside_area(line_idx, char_idx):
    u_range = range(line_idx, min_x-1, -1)
    d_range = range(line_idx, max_x+1)
    l_range = range(char_idx, min_y-1, -1)
    r_range = range(char_idx, max_y+1)

    up_list = set(list(zip_longest(u_range, [char_idx], fillvalue=char_idx)))
    down_list = set(list(zip_longest(d_range, [char_idx], fillvalue=char_idx)))
    right_list = set(list(zip_longest([line_idx], r_range, fillvalue=line_idx)))
    left_list = set(list(zip_longest([line_idx], l_range, fillvalue=line_idx)))
    summary = [len(coords_set.intersection(a))>0 for a in [up_list, down_list, right_list, left_list]]
    if all(summary):
        return True
    pass


for  char_idx in range(min_x-1, max_x+2):
    for line_idx in range(min_y-1, max_y+2):
        if check_if_inside_area(char_idx, line_idx):
            #coords_set.add((line_idx, char_idx))
            coords_set.add((char_idx, line_idx))
plt.scatter([item[0] for item in list(coords_set)], [item[1] for item in list(coords_set)])
plt.show() 
print(len(coords_set))
# 35630 too low
# 76913 too high
pass