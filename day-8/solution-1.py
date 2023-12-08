from pathlib import Path
import os
from collections import Counter

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

lr_list = [0 if x == "L" else 1 for x in file_lines_list[0]]

nav_pairs = {
    "L": 0,
    "R": 1
}

line_dict = {}
for index, line in enumerate(file_lines_list[2:]):
    cur = line.split("=")[0].strip()
    left = line.split("=")[1].replace(")", "").replace("(", "").replace(",", "").split()[0]
    right = line.split("=")[1].replace(")", "").replace("(", "").replace(",", "").split()[1]
    line_dict.update({cur: (left, right)})

#cur_location = list(line_dict.keys())[0]
cur_location = "AAA"

number_of_steps = 0
while cur_location != "ZZZ":
    cur_next_elem_l_or_r = lr_list[number_of_steps % len(lr_list)]
    cur_location = line_dict[cur_location][cur_next_elem_l_or_r]
    number_of_steps += 1
    pass

# 19951
print(number_of_steps)
