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

total_number_of_cards = len(file_lines_list)
cards_with_won_cards = []
for index, line in enumerate(file_lines_list):
    numbers_i_have = set([int(number) for number in line.split(":")[-1].split("|")[0].split()])
    winning_numbers = set([int(number) for number in line.split(":")[-1].split("|")[1].split()])
    intersect = numbers_i_have.intersection(winning_numbers)
    current_card_value = int(2**(len(intersect)-1))
    won_no_of_cards = len(intersect)
    cards_with_won_cards.append({index+1: [i for i in range(index+2, index+2+won_no_of_cards)]})

i = 0
while True:
    
    i += 1