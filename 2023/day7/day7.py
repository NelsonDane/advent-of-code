# Nelson Dane
# Advent of Code 2023 Day 7

import sys
from collections import Counter
from functools import cmp_to_key

# Get input args
filename = 'input.txt'
if len(sys.argv) == 2 and "e" in sys.argv[1]:
    filename = 'example.txt'
SHOULD_PRINT = False
if len(sys.argv) == 2 and "p" in sys.argv[1]:
    SHOULD_PRINT = True
DEBUG_LOG = False
if len(sys.argv) == 2 and "l" in sys.argv[1]:
    DEBUG_LOG = True

# Read in the input file
with open(filename, 'r') as f:
    data = f.read().splitlines()

def print_and_log(message):
    if SHOULD_PRINT:
        print(message)
    if DEBUG_LOG:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f"{message}\n")

FIVE_OF_A_KIND = 1
FOUR_OF_A_KIND = 2
FULL_HOUSE = 3
THREE_OF_A_KIND = 4
TWO_PAIR = 5
PAIR = 6
HIGH_CARD = 7
RANK_ORDER = "23456789TJQKA"
RANK_ORDER_JOKER = "J23456789TQKA"

def get_type(game, joker=False):
    hand = list(game['hand'])
    counts = Counter(hand)
    if joker:
        jokers = 0
        if "J" in counts:
            jokers = counts["J"]
            del counts["J"]
            if jokers == 5:
                return FIVE_OF_A_KIND
        if jokers > 0:
            counts = dict(counts)
            counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
            counts[next(iter(counts))] += jokers        
    counts_check = len(counts)
    if counts_check == 1:
        return FIVE_OF_A_KIND
    elif counts_check == 2:
        if 4 in counts.values():
            return FOUR_OF_A_KIND
        else:
            return FULL_HOUSE
    elif counts_check == 3:
        if 3 in counts.values():
            return THREE_OF_A_KIND
        else:
            return TWO_PAIR
    elif counts_check == 4:
        return PAIR
    else:
        return HIGH_CARD

def hand_compare(hand1, hand2, joker=False):
    if hand1['type'] < hand2['type']:
        return -1
    elif hand1['type'] > hand2['type']:
        return 1
    for i in range(5):
        hand1_char = hand1['hand'][i]
        hand2_char = hand2['hand'][i]
        if joker:
            hand1_rank = RANK_ORDER_JOKER.index(hand1_char)
            hand2_rank = RANK_ORDER_JOKER.index(hand2_char)
        else:
            hand1_rank = RANK_ORDER.index(hand1_char)
            hand2_rank = RANK_ORDER.index(hand2_char)
        if hand1_rank < hand2_rank:
            return 1
        elif hand1_rank > hand2_rank:
            return -1
    return 0

def compare(hand1, hand2):
    return hand_compare(hand1, hand2)

def compare_joker(hand1, hand2):
    return hand_compare(hand1, hand2, joker=True)

# Part 1
game = {
    "hand": "",
    "bid": int(),
    "type": int(),
    "rank": int(),
    "winnings": int()
}
games = []
for line in data:
    game['hand'] = line.split(' ')[0]
    game['bid'] = int(line.split(' ')[1])
    game['type'] = get_type(game)
    games.append(game.copy())
games = sorted(games, key=cmp_to_key(compare))
total_winnings = 0
for i, game in enumerate(games):
    game['rank'] = len(games) - i
    game['winnings'] = game['rank'] * game['bid']
    total_winnings += game['winnings']
print_and_log(games)
print(f"Part 1: {total_winnings}")

# Part 2 (Joker)
for game in games:
    game['type'] = get_type(game, joker=True)
games = sorted(games, key=cmp_to_key(compare_joker))
total_winnings = 0
for i, game in enumerate(games):
    game['rank'] = len(games) - i
    game['winnings'] = game['rank'] * game['bid']
    total_winnings += game['winnings']
print_and_log(games)
print(f"Part 2: {total_winnings}")
