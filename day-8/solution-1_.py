from pathlib import Path
import os
from collections import Counter

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

card_values = {
"A": 14,
"K": 13,
"Q": 12,
"J": 11,
"T": 10,
"9": 9,
"8": 8,
"7": 7,
"6": 6,
"5": 5,
"4": 4,
"3": 3,
"2": 2,
}

print(int(0xF))
card_values = {
"A": "E",
"K": "D",
"Q": "C",
"J": "B",
"T": "A",
"9": "9",
"8": "8",
"7": "7",
"6": "6",
"5": "5",
"4": "4",
"3": "3",
"2": "2",
}

def get_hand_value(hand: str):
    converted_to_hex = "".join([card_values[i] for i in hand])
    hex_to_int = int(converted_to_hex, base=16)
    return hex_to_int

get_hand_value("AA")

list_of_hands = []
for index, line in enumerate(file_lines_list):
    hand = line.split()[0]
    bet = int(line.split()[1])
    hand_counted = Counter(hand)
    counted_len = len(hand_counted)
    list_of_card_amounts = hand_counted.values()

    match counted_len:
        case 1:
            # Five of a kind
            hand_rank = 7
        case 2:
            if 4 in list_of_card_amounts:
                # Four of a kind
                hand_rank = 6
            else:
                # Full house
                hand_rank = 5
        case 3:
            # Three of a kind
            if 3 in list_of_card_amounts:
                hand_rank = 4
            else:
                hand_rank = 3
        case 4:
            hand_rank = 2
        case 5:
            hand_rank = 1

    list_of_hands.append((hand, bet, 100000000000000*hand_rank, get_hand_value(hand)))

sorted_list = sorted(list_of_hands, key=lambda x: x[2]+x[3])

final = [(i+1)*x[1] for i, x in enumerate(sorted_list)]
print(sum(final))
