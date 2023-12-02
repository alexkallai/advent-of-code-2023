from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

sum_of_all_games_indeces = sum(list(range(1, len(file_lines_list)+1)))

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

not_possible_games = []
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

# Game number starts from 1 !!!
for index, line in enumerate(file_lines_list):
    line_data = get_game_data(line)
    games.append(line_data)

for index, game in enumerate(games):
    game_no = index + 1
    broken = False
    for draws in game:
        if broken:
            break
        for cube_draw in draws:
            color = cube_draw[0]
            number = cube_draw[1]
            if not number <= cubes[color]:
                not_possible_games.append(game_no)
                broken = True
                break

print(sum_of_all_games_indeces-sum(not_possible_games))
