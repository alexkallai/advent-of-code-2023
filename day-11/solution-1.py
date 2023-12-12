from pathlib import Path
import os
from collections import Counter
from itertools import combinations
import copy

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

height = len(file_lines_list)
width = len(file_lines_list[0])
galaxy_matrix = [[file_lines_list[w][h] for h in range(height)] for w in range(width)]

# Get empty rows and columns
empty_rows = []
empty_cols = []
for index, line in enumerate(galaxy_matrix):
    if not "#" in line:
        empty_rows.append(index)
for index, col in enumerate(zip(*galaxy_matrix)):
    if not "#" in col:
        empty_cols.append(index)

# Insert rows
for index, row in enumerate(empty_rows):
    galaxy_matrix.insert(row+index, ["." for _ in range(width)])

for index, col in enumerate(empty_cols):
    for i2, row in enumerate(galaxy_matrix):
        galaxy_matrix[i2].insert(col+index, ".")

# Galaxy expanded
def manhattan(x1, y1, x2, y2):
    return abs((x1-x2)) + abs(y1-y2)

list_of_galaxies = []
for line_idx, line in enumerate(galaxy_matrix):
    for col_idx, element in enumerate(line):
        if galaxy_matrix[line_idx][col_idx] == "#":
            list_of_galaxies.append((line_idx, col_idx))

list_of_distances = []
for index, pair in enumerate(combinations(list_of_galaxies, 2)):
    #print(index+1, pair)
    list_of_distances.append(manhattan(pair[0][0], pair[0][1], pair[1][0], pair[1][1],))

print(sum(list_of_distances))
