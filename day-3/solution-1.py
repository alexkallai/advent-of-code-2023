from pathlib import Path
import os
import re

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

width = len(file_lines_list[0])
height = len(file_lines_list)

def is_symbol(char: str):
    if not char.isnumeric() and not char == ".":
        return True
    else:
        return False

def is_number_adjecent_to_symbol(x, y, number):
    number_len = len(str(number))
    # same line as number:
    if x>0:
        if is_symbol(file_lines_list[y][x-1]):
            return True
    fol_char_x_idx = x+number_len
    if fol_char_x_idx<width:
        if is_symbol(file_lines_list[y][x+number_len]):
            return True
    # previous line
    if y>0:
        from_idx = x-1 if x>0 else x
        until_idx = x+number_len if x+number_len<width else x+number_len-1
        for index in range(from_idx, until_idx+1):
            if is_symbol(file_lines_list[y-1][index]):
                return True
    # next line
    if y<height-1:
        from_idx = x-1 if x>0 else x
        until_idx = x+number_len if x+number_len<width else x+number_len-1
        for index in range(from_idx, until_idx+1):
            if is_symbol(file_lines_list[y+1][index]):
                return True

def get_numbers_from_line(line):
    matches = re.finditer(r'\d+', line)
    numbers = [(match.group(), match.start()) for match in matches]
    return numbers

numbers_to_add = []
for line_no, line in enumerate(file_lines_list):
    list_of_numbers_in_line = get_numbers_from_line(line)
    for result in list_of_numbers_in_line:
        number = int(result[0])
        number_x_coord = result[1]
        if is_number_adjecent_to_symbol(number_x_coord, line_no, number):
            numbers_to_add.append(number)

print(sum(numbers_to_add))
