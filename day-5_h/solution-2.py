from pathlib import Path
import os
from functools import cache

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

seeds = [int(i) for i in file_lines_list[0].split(":")[1].split()]
paired_seeds = [(seeds[i],seeds[i + 1]) for i in range(0, len(seeds), 2)]
paired_seeds_ranges = [range(item[0], item[0]+item[1], 1) for item in paired_seeds]

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

#@cache
def get_mapped_value(value, map):
    for line in maps[map]:
        if line[1] <= value <= line[1]+line[2]:
            return value-line[1]+line[0]
    return value

@cache
def get_location_from_seed(seed):
    mapped_value = seed
    for map in maps.keys():
        mapped_value = get_mapped_value(mapped_value, map)
    return mapped_value

min_value = 999999999999999999999999999
for index, seeds_ in enumerate(paired_seeds_ranges):
    print(f"Calculating range {index} of {len(paired_seeds_ranges)}")
    for seed in seeds_:
        mapped_value = get_location_from_seed(seed)
        min_value = min(min_value, mapped_value)

print(min_value)
