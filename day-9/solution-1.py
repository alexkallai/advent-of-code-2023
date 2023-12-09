from pathlib import Path
import os
from collections import Counter
from itertools import pairwise

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

def get_next_value_for_history(history: list[int]):
    list_of_number_lists = []
    list_of_number_lists.append(history)
    while True:
        next_line = [x[1] - x[0] for x in pairwise(list_of_number_lists[-1])]
        list_of_number_lists.append(next_line)
        if len(set(next_line)) == 1 and next_line[0] == 0:
            break
    list_of_number_lists.reverse()
    for index, line in enumerate(list_of_number_lists):
        if index == 0:
            list_of_number_lists[index].append(0)
            continue
        list_of_number_lists[index].append(list_of_number_lists[index][-1] + list_of_number_lists[index-1][-1])
    return list_of_number_lists[-1][-1]


history_list = []
for index, line in enumerate(file_lines_list):
    history_list.append([int(i) for i in line.split()])

results = []
for index, history in enumerate(history_list):
    results.append(get_next_value_for_history(history))

print(sum(results))