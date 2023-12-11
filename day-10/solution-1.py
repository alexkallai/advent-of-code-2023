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

class FieldElement:
    
    def __init__(self, char, masked, distance) -> None:
        self.char = char
        self.masked = masked
        self.distance = distance
    
    def __repr__(self) -> str:
        return self.char

    def __str__(self) -> str:
        return f"{self.char}, {self.masked}, {self.distance}"

field: list[list[FieldElement]] = [[None for _ in range(height)] for _ in range(width)]
for index, line in enumerate(file_lines_list):
    for i2, char in enumerate(line):
        field[index][i2] = FieldElement(char, False, None)

# order: x, y > x is horizontal
val_nb_dict = {
    "|": ((0,-1), (0,1)),
    "-": ((-1,0), (1,0)),
    "L": ((0,-1), (1,0)),
    "J": ((0,-1), (-1,0)),
    "F": ((0,1), (1,0)),
}
# . is ground
# S is starting point
starting_point = None
for index, line in enumerate(file_lines_list):
    if "S" in line:
        starting_point = (line.index("S"), index)

def print_matrix(cur_coords:tuple, checked_coords: tuple):
    #copied_matrix = copy.deepcopy(file_lines_list)
    copied_matrix = copy.deepcopy(field)
    for i1, line in enumerate(copied_matrix):
        for i2, _ in enumerate(line):
            if i1 == checked_coords[1] and i2 == checked_coords[0]:
                copied_matrix[i1][i2].char =  "▮"
            if i1 == cur_coords[1] and i2 == cur_coords[0]:
                copied_matrix[i1][i2].char =  "?"
        print(line)
    print("")

#mask_matrix[starting_point[1]][starting_point[0]] = True
def is_neighbour_valid(x_coord, y_coord):
    if 0 <= x_coord < width and 0 <= y_coord < height and field[y_coord][x_coord].masked == False:
        checked_nb_char = field[y_coord][x_coord].char
        print(f"Checked char: {checked_nb_char}")
        if checked_nb_char in val_nb_dict.keys():
            return True
    return False


def get_first_valid_neighbour(coordinate: tuple):
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if not (x == 0 and y == 0):
                x_coord = coordinate[0] + x
                y_coord = coordinate[1] + y
                #print(x_coord, y_coord)
                if is_neighbour_valid(x_coord, y_coord):
                    checked_nb_char = field[y_coord][x_coord].char
                    for neighbour in val_nb_dict[checked_nb_char]:
                        neighbour_tuple = (x_coord+neighbour[0], y_coord+neighbour[1])
                        if 0 <= neighbour_tuple[1] < height and 0 <= neighbour_tuple[0] < width:
                            print_matrix(cur_coords=coordinate ,checked_coords=neighbour_tuple)
                            if neighbour_tuple  == coordinate:
                                field[y_coord][x_coord].masked = True
                                field[y_coord][x_coord].distance = runner
                                return (x_coord, y_coord)
                    if checked_nb_char == "S" and runner > 2:
                        return -1
    print("ERROR")

#get_first_valid_neighbour(starting_point)
curr_coord = None
runner = 0
while curr_coord != starting_point:
    # Init step
    if curr_coord == None:
        curr_coord = starting_point
        field[curr_coord[1]][curr_coord[0]].masked = True
        runner += 1

    curr_coord = get_first_valid_neighbour(curr_coord)
    if curr_coord == -1:
        break
    runner += 1
    #print(runner)

pass

