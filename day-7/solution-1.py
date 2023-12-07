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

card_strengths = [
"A",
"K",
"Q",
"J",
"T",
"9",
"8",
"7",
"6",
"5",
"4",
"3",
"2",
]
card_strengths.reverse()

def get_value(card_type):
    return card_strengths.index(card_type)+1

hands_strength_dict = {
    "Five of a kind": 7,
    "Four of a kind": 6,
    "Full house": 5,
    "Three of a kind": 4,
    "Two pair": 3,
    "One pair": 2,
    "High card": 1,
}

cards_dict = {}

def order_same_type_hands(list_of_hands):
    ordered_list = []
    current_values = []
    def custom_sort_key(sublist):
    # Multiply each element by a decreasing weight, with the highest weight for the first element
        calculated_value = tuple(get_value(val) * (10 ** (len(sublist) - i - 1)) for i, val in enumerate(sublist))
        return calculated_value

    ordered_list = sorted(list_of_hands, key=custom_sort_key)
    ordered_list.reverse()
    return ordered_list
    #for i in range(5):
        #current_values = [get_value(sublist[0]) for index, sublist in enumerate(list_of_hands)]
        #if len(set(current_values)) == len(list_of_hands):
            #break



order_same_type_hands([
    "32T3K",
    "T55J5",
    "KK677",
    "KTJJT",
    "QQQJA",
])

hands_with_bids = {}

for index, line in enumerate(file_lines_list):
    hand = line.split()[0]
    bid = int(line.split()[1])
    hands_with_bids.update({hand: bid})
    analyzed_hand = Counter(hand)
    len_analyzed_hand = len(analyzed_hand)
    match len_analyzed_hand:
        case 1:
            hand_type = "Five of a kind"
        case 2:
            if analyzed_hand[0] == 1 or analyzed_hand[0] == 4:
                hand_type = "Four of a kind"
            if analyzed_hand[0] == 2 or analyzed_hand[0] == 3:
                hand_type = "Full house"
        case 3:
            # TODO
            if 3 in analyzed_hand.values():
                hand_type = "Three of a kind"
            else:
                hand_type = "Two pair"
        case 4:
            hand_type = "One pair"
        case 5:
            hand_type = "High card"
    cards_dict.update({hand: hands_strength_dict[hand_type]})
    print(hand)
    print(analyzed_hand)
    print(hand_type)

#print(cards_dict)

sorted_list_of_cards = sorted(cards_dict.items(), key=lambda x: x[1])
sorted_list_of_cards.reverse()

correctly_sorted_cards = []
for no in range(7, 0, -1):
    unordered_sublist = [hand for hand, rank in sorted_list_of_cards if rank == no]
    ordered_sublist = order_same_type_hands(unordered_sublist)
    correctly_sorted_cards.extend(ordered_sublist)

# 251420749 too high
# 251382306 too high
# 249618194 too low
print(correctly_sorted_cards)
correctly_sorted_cards.reverse()
result_list = [(i+1)*hands_with_bids[hand] for i, hand in enumerate(correctly_sorted_cards)]
print(sum(result_list))
