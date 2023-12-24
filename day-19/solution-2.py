from pathlib import Path
import os
from collections import Counter
from itertools import pairwise, zip_longest
from binarytree import Node, tree

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



cur_workflow = "in"
binlist = workflows[cur_workflow]
while True:
    binlistlen = len(binlist)
    for i in range(binlistlen):
        if isinstance(binlist[i], str):
            next = binlist[i].split(":")[-1]
            binlist[i] = [binlist[i], *workflows[next]]
            pass

        if isinstance(binlist[i], list):
            pass



# bintree = Node(workflows[cur_workflow][0])