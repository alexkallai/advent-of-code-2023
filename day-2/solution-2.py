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

sum_of_all_games_indeces = sum(list(range(1, len(file_lines_list)+1)))

game_powers = []
games = []

def get_game_data(line: str):
    game_cubes_subsets: list[str] = line.split(":")[-1].strip().split(";")
    for index, subset in list(enumerate(game_cubes_subsets)):
        game_cubes_subsets[index] = subset.split(",")
        for index2, type_of_balls in list(enumerate(game_cubes_subsets[index])):
            number = int(game_cubes_subsets[index][index2].strip().split(" ")[0].strip())
            color = game_cubes_subsets[index][index2].strip().split(" ")[1].strip()
            game_cubes_subsets[index][index2] = [color, number]
    return game_cubes_subsets

def power(minimum_no_of_cubes_list: list):
    power_no = 1
    for number in minimum_no_of_cubes_list:
        power_no = power_no * number
    return power_no

# Game number starts from 1 !!!
for index, line in enumerate(file_lines_list):
    line_data = get_game_data(line)
    games.append(line_data)

for index, game in enumerate(games):
    min_no_of_cubes = {}
    game_no = index + 1
    for draws in game:
        for cube_draw in draws:
            color = cube_draw[0]
            number = cube_draw[1]
            min_no_of_cubes[color] = max(min_no_of_cubes[color], number) if color in min_no_of_cubes.keys() else max(0, number)
    game_powers.append(power(min_no_of_cubes.values()))

print(sum(game_powers))



