# Nelson Dane
# Advent of Code 2023 Day 2

import json

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

def get_all_games(data):
    all_games_dict = {}
    for game in data:
        game_dict = {}
        game_num = game.split(':')[0].split(' ')[-1]
        game_sets = game.split(':')[1].split(';')
        for i, game_set in enumerate(game_sets):
            i += 1
            game_set_dict = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            game_set = game_set.split(',')
            game_set = [x.strip() for x in game_set]
            for item in game_set:
                game_set_dict[item.split(' ')[1]] = int(item.split(' ')[0])
            game_dict[i] = game_set_dict
        all_games_dict[game_num] = game_dict
    # print(json.dumps(all_games_dict, indent=4))
    return all_games_dict

# Part 1
limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

all_games_dict = get_all_games(data)

# Apply limits
possible_games = {}
for game_num, game in all_games_dict.items():
    game_possible = True
    for game_set_num, game_set in game.items():
        for color, value in game_set.items():
            if value > limits[color]:
                game_possible = False
                break
    if game_possible:
        possible_games[game_num] = game

print(f'Possible games: {len(possible_games)}')
# for game in possible_games:
#     print(game)
print(f"Sum: {sum([int(x) for x in possible_games])}")

# Part 2
all_games_dict = get_all_games(data)

# Get minimum needed for each game
minimums = {}
for game_num, game in all_games_dict.items():
    min_colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for game_set_num, game_set in game.items():
        for color, value in game_set.items():
            if value > min_colors[color]:
                min_colors[color] = value
    minimums[game_num] = min_colors

# Calculate power
for game_num, game in minimums.items():
    power = 1
    for value in game.values():
        power *= value
    minimums[game_num]['power'] = power

print(json.dumps(minimums, indent=4))
print(f"Sum: {sum([int(x['power']) for x in minimums.values()])}")
