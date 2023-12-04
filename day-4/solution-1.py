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

cards_list_values = []
for index, line in enumerate(file_lines_list):
    numbers_i_have = set([int(number) for number in line.split(":")[-1].split("|")[0].split()])
    winning_numbers = set([int(number) for number in line.split(":")[-1].split("|")[1].split()])
    #print(numbers_i_have)
    #print(winning_numbers)
    intersect = numbers_i_have.intersection(winning_numbers)
    print(intersect)
    current_card_value = int(2**(len(intersect)-1))
    print(current_card_value)
    cards_list_values.append(current_card_value)

# 15268
print(sum(cards_list_values))
