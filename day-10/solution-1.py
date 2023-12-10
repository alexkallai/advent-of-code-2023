from pathlib import Path
import os
from collections import Counter
from itertools import pairwise
import copy

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN
width = len(file_lines_list[0])
height = len(file_lines_list)
mask_matrix = [[False for _ in range(height)] for _ in range(width)]


# order: x, y > x is horizontal
val_nb_dict = {
    "|": ((0,-1), (0,1)),
    "-": ((-1,0), (1,0)),
    "L": ((1,1), (1,0)),
    "J": ((1,1), (-1,0)),
    "F": ((0,-1), (1,0)),
}
# . is ground
# S is starting point
starting_point = None
for index, line in enumerate(file_lines_list):
    if "S" in line:
        starting_point = (line.index("S"), index)

#mask_matrix[starting_point[1]][starting_point[0]] = True

def get_first_valid_neighbour(coordinate: tuple):
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if not (x == 0 and y == 0):
                x_coord = coordinate[0] + x
                y_coord = coordinate[1] + y
                #print(x_coord, y_coord)
                if 0 <= x_coord < width and 0 <= y_coord < height and mask_matrix[y_coord][x_coord] == False:
                    checked_nb = file_lines_list[y_coord][x_coord]
                    print(checked_nb)
                    if checked_nb in val_nb_dict.keys():
                        for neighbour in val_nb_dict[checked_nb]:
                            if (x_coord+neighbour[0], y_coord+neighbour[1]) == coordinate:
                                mask_matrix[y_coord][x_coord] = True
                                return (x_coord, y_coord)

#get_first_valid_neighbour(starting_point)
curr_coord = None
runner = 0
while curr_coord != starting_point:
    # Init step
    if curr_coord == None:
        curr_coord = starting_point

    curr_coord = get_first_valid_neighbour(curr_coord)
    runner += 1
    print(runner)


