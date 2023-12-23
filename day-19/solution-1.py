from pathlib import Path
import os
from collections import Counter
from itertools import pairwise, zip_longest

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

split_line_no = None
for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
    if file_lines_list[index] == "":
        split_line_no = index

# FILE READ IN

def sum_part_rating(part):
    return sum(part.values())

workflows = {}
for index, line in enumerate(file_lines_list[0:split_line_no]):
    workflow_name = line.split("{")[0]
    content_list = line.split("{")[1][:-1].split(",")
    workflows.update({workflow_name: content_list})
    pass

part_ratings = []
for index, line in enumerate(file_lines_list[split_line_no+1:]):
    print(line)
    part_dict = {}
    for i in line[1:-1].split(","):
        part_dict.update({i.split("=")[0]: int(i.split("=")[1])})
    part_ratings.append(part_dict)

def parse_check(check):
    global cur_workflow
    if "A" == check or "R" == check:
        cur_workflow = check
        return None
    if ":" not in check:
        cur_workflow = check
        return 1
    else:
        expr = check.split(":")[0]
        print(f"? {expr}")
        if eval(expr):
            cur_workflow = check.split(":")[1]
            print(f"True -> {cur_workflow}")
            return True
        print("False")
        return False


accepted_parts_sums = 0
for index, part in enumerate(part_ratings):
    print("***********************")
    print(f"PART {index}")
    print(f"{part}")
    print("***********************")

    cur_sum = sum_part_rating(part)
    # Declare vars
    for val in part.keys():
        expression = str(f"{val} = {part[val]}")
        exec(expression)

    cur_workflow = "in"
    while cur_workflow != "A" and cur_workflow != "R":
        print(cur_workflow)
        for check in workflows[cur_workflow]:
            res = parse_check(check)
            if res == None or res == True:
                break

    if cur_workflow == "A":
        accepted_parts_sums += cur_sum
        continue
    if cur_workflow == "R":
        continue


print((accepted_parts_sums))

pass