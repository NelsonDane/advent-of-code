# Nelson Dane
# Advent of Code 2023 Day 4

import sys

# Get input args
filename = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'e':
    filename = 'example.txt'

# Read in the input file
with open(filename, 'r') as f:
    data = f.read().splitlines()

def calculate_score(list_of_winning_numbers):
    if len(list_of_winning_numbers) == 0:
        return 0
    else:
        # 2 ^ (n - 1)
        return 2 ** (len(list_of_winning_numbers) - 1)
    
# Part 1
data_list = []
winning_sum = 0
for card in data:
    # Card dict for part 2
    card_dict = {
        'card_num': None,
        'winning_nums': [],
        'instances': 1
    }
    card_num = int(card.split(':')[0].split(' ')[-1].strip())
    numbers = card.split(':')[1]
    game_nums = numbers.split(' | ')[0].split(' ')
    game_nums = [x for x in game_nums if x != '']
    my_nums = numbers.split(' | ')[1].split(' ')
    my_nums = [x for x in my_nums if x != '']
    # Find overlap
    winning_nums = set(game_nums).intersection(set(my_nums))
    # print(f"Game {card_num}: Game Numbers: {game_nums}, My Numbers: {my_nums}, Winning Numbers: {winning_nums}, Score: {calculate_score(winning_nums)}")
    winning_sum += calculate_score(winning_nums)
    card_dict['card_num'] = card_num
    card_dict['winning_nums'] = winning_nums
    data_list.append(card_dict)

print(f"Part 1: {winning_sum}")

# Part 2
for card_index, card_dict in enumerate(data_list):
    amount_won = len(card_dict['winning_nums'])
    # print(f"Card {card_dict['card_num']} ({card_dict['instances']}) won {amount_won} times")
    for i in range(1, amount_won + 1):
        # print(f"Incrementing card {data_list[card_index + i]['card_num']} by {card_dict['instances']}")
        data_list[card_index + i]['instances'] += card_dict['instances']

# print(data_list)
print(f"Part 2: {sum([x['instances'] for x in data_list])}")
