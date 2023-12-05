from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

seeds = [int(i) for i in file_lines_list[0].split(":")[1].split()]
maps = {}
cur_key = ""
for index, line in enumerate(file_lines_list[2:]):
    if line != "":
        if line[0].isalpha():
            cur_key = line
        if line[0].isdigit() and cur_key in maps.keys():
            maps[cur_key].append([int(i) for i in line.split()])
        if line[0].isdigit() and not cur_key in maps.keys():
            maps.update({cur_key: [[int(i) for i in line.split()]]})

def get_mapped_value(value, map):
    for line in map:
        if line[1] <= value <= line[1]+line[2]:
            return value-line[1]+line[0]
    return value

mapped_values = []
for seed in seeds:
    mapped_value = seed
    for map in maps.keys():
        mapped_value = get_mapped_value(mapped_value, maps[map])
    mapped_values.append(mapped_value)

print(min(mapped_values))
