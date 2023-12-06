from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

times = [ int(i) for i in file_lines_list[0].split(":")[1].split()]
distances = [ int(i) for i in file_lines_list[1].split(":")[1].split()]

zipped = zip(times, distances)

def calculate_distance(race_time, acceleration_time):
    travel_time = race_time - acceleration_time
    travel_speed = acceleration_time
    distance = travel_time * travel_speed
    return distance

acceleration = 1 # mm/s
list_of_results = []
for race in zipped:
    number_of_correct_results = 0
    race_time_ms = race[0]
    race_record_distance_mm = race[1]

    for acceleration_time in range(0, race_time_ms, 1):
        cur_distance = calculate_distance(race_time_ms, acceleration_time)
        if cur_distance > race_record_distance_mm:
            number_of_correct_results += 1
    list_of_results.append(number_of_correct_results)
res = 1
for i in list_of_results:
    res = res * i

print(res)