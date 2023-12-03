# Nelson Dane
# Advent of Code 2023 Day 3

import json

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

def is_symbol(char):
    if char.isnumeric() or char == '.':
        return False
    return True

def get_previous_line(index, data):
    previous_line = None
    try:
        if index > 0:
            previous_line = data[index - 1]
    except IndexError:
        pass
    return previous_line

def get_next_line(index, data):
    try:
        next_line = data[index + 1]
    except IndexError:
        next_line = None
    return next_line

def get_line_char(index, line):
    char = None
    try:
        if line is not None and index >= 0 and index < len(line):
            char = line[index]
    except IndexError:
        pass
    return char

def get_surrounding_chars(char_index, line_index, line, data):
    previous_line = get_previous_line(line_index, data)
    next_line = get_next_line(line_index, data)
    # Get char before, after, above, below, and diagonal
    # Before
    if char_index > 0:
        char_before = get_line_char(char_index - 1, line)
    else:
        char_before = None
    # After
    char_after = get_line_char(char_index + 1, line)
    # Above
    char_above = get_line_char(char_index, previous_line)
    # Below
    char_below = get_line_char(char_index, next_line)
    # Diagonal upper left
    char_diagonal_upper_left = get_line_char(char_index - 1, previous_line)
    # Diagonal upper right
    char_diagonal_upper_right = get_line_char(char_index + 1, previous_line)
    # Diagonal lower left
    char_diagonal_lower_left = get_line_char(char_index - 1, next_line)
    # Diagonal lower right
    char_diagonal_lower_right = get_line_char(char_index + 1, next_line)
    return [
        char_before,
        char_after,
        char_above,
        char_below,
        char_diagonal_upper_left,
        char_diagonal_upper_right,
        char_diagonal_lower_left,
        char_diagonal_lower_right,
    ]

def is_char_symbol_adjacent(char_index, line_index, line, data):
    testing_char = line[char_index]
    surrounding_chars = get_surrounding_chars(char_index, line_index, line, data)
    char_before = surrounding_chars[0]
    char_after = surrounding_chars[1]
    char_above = surrounding_chars[2]
    char_below = surrounding_chars[3]
    char_diagonal_upper_left = surrounding_chars[4]
    char_diagonal_upper_right = surrounding_chars[5]
    char_diagonal_lower_left = surrounding_chars[6]
    char_diagonal_lower_right = surrounding_chars[7]
    # Check if any are symbols
    for char in [char_before, char_after, char_above, char_below, char_diagonal_upper_left, char_diagonal_upper_right, char_diagonal_lower_left, char_diagonal_lower_right]:
        if char is not None:
            if is_symbol(char):
                # print(f"{testing_char} is adjacent to {char}")
                return True
    return False

def traverse_line_for_numbers(num_index, line_index, data):
    # Traverse the line in until it's pulled single complete number
    line = data[line_index]
    num = line[num_index]
    num_group = []
    start_index = num_index
    # Find leftmost number
    while num.isnumeric() and start_index >= 0:
        start_index -= 1
        num = line[start_index]
    # print(f"Start Index: {start_index}, Num: {line[start_index]}")
    # Traverse left
    num_index_temp = start_index + 1
    num = line[num_index_temp]
    while num.isnumeric():
        num_group.append(num)
        num_index_temp += 1
        try:
            num = line[num_index_temp]
        except IndexError:
            break
    number = ''.join(num_group)
    # print(f"Number: {number}")
    return number

def is_number(char):
    if char is not None and char.isnumeric():
        return True
    return False

def is_char_number_adjacent(char_index, line_index, line, data):
    # We need 2 adjacent numbers
    testing_char = line[char_index]
    surrounding_chars = get_surrounding_chars(char_index, line_index, line, data)
    char_before = {
        'char': surrounding_chars[0],
        'index': char_index - 1,
        'line_index': line_index,
    }
    char_after = {
        'char': surrounding_chars[1],
        'index': char_index + 1,
        'line_index': line_index,
    }
    char_above = {
        'char': surrounding_chars[2],
        'index': char_index,
        'line_index': line_index - 1,
    }
    char_below = {
        'char': surrounding_chars[3],
        'index': char_index,
        'line_index': line_index + 1,
    }
    char_diagonal_upper_left = {
        'char': surrounding_chars[4],
        'index': char_index - 1,
        'line_index': line_index - 1,
    }
    char_diagonal_upper_right = {
        'char': surrounding_chars[5],
        'index': char_index + 1,
        'line_index': line_index - 1,
    }
    char_diagonal_lower_left = {
        'char': surrounding_chars[6],
        'index': char_index - 1,
        'line_index': line_index + 1,
    }
    char_diagonal_lower_right = {
        'char': surrounding_chars[7],
        'index': char_index + 1,
        'line_index': line_index + 1,
    }
    # Check if any are numbers
    num_1_found = False
    num_1 = None
    num_2_found = False
    num_2 = None
    adjacent_numbers = []
    for char_dict in [char_before, char_after, char_above, char_below, char_diagonal_upper_left, char_diagonal_upper_right, char_diagonal_lower_left, char_diagonal_lower_right]:
        if char_dict['char'] is not None:
            char = char_dict['char']
            if char.isnumeric():
                num = traverse_line_for_numbers(char_dict['index'], char_dict['line_index'], data)
                adjacent_numbers.append(num)
    # Remove duplicates
    adjacent_numbers = list(set(adjacent_numbers))
    # Must have exactly 2 adjacent numbers
    if len(adjacent_numbers) == 2:
        num_1 = adjacent_numbers[0]
        num_2 = adjacent_numbers[1]
        num_1_found = num_2_found = True
    # if num_1_found and num_2_found:
        # print(f"{testing_char} is adjacent to {num_1} and {num_2}")
    return num_1_found and num_2_found, num_1, num_2

# Part 1
sym_adj_numbers = []    
not_sym_adj_numbers = []
for line in data:
    line_dict = {}
    # print(line)
    for i, char in enumerate(line):
        test_dict = {
            'char': None,
            'index': None,
            'symbol_adjacent': False,
        }
        test_dict['index'] = i
        test_dict['char'] = char
        is_sym_adj = is_char_symbol_adjacent(i, data.index(line), line, data)
        if is_sym_adj:
            test_dict['symbol_adjacent'] = True
        line_dict[i] = test_dict
    # Group numbers
    group = {
        'numbers': [],
        'symbol_adjacent': False,
    }
    for i, char_dict in line_dict.items():
        char = char_dict['char']
        if char.isnumeric():
            group['numbers'].append(char)
            if char_dict['symbol_adjacent']:
                group['symbol_adjacent'] = True
        else:
            if len(group['numbers']) > 0:
                if group['symbol_adjacent']:
                    sym_adj_numbers.append(''.join(group['numbers']))
                else:
                    not_sym_adj_numbers.append(''.join(group['numbers']))
                group = {
                    'numbers': [],
                    'symbol_adjacent': False,
                }
    # Don't forget to check the last group, this could be done better
    if len(group['numbers']) > 0:
        if group['symbol_adjacent']:
            sym_adj_numbers.append(''.join(group['numbers']))
        else:
            not_sym_adj_numbers.append(''.join(group['numbers']))
    
# Part 2
num_adjcent_stars = []
not_num_adjcent_stars = []
for line in data:
    line_dict = {}
    for i, char in enumerate(line):
        test_dict = {
            'star': False,
            'index': None,
            'line_index': None,
            'num_adjacent_1': False,
            'num_adjacent_2': False,
            'num_1': None,
            'num_2': None,
            'gear_ratio': None,
        }
        if char == '*':
            test_dict['index'] = i
            test_dict['line_index'] = data.index(line)
            test_dict['star'] = True
            is_num_adj, num_1, num_2 = is_char_number_adjacent(i, data.index(line), line, data)
            if is_num_adj:
                test_dict['num_adjacent_1'] = True
                test_dict['num_1'] = num_1
                test_dict['num_adjacent_2'] = True
                test_dict['num_2'] = num_2
                test_dict['gear_ratio'] = int(num_1) * int(num_2)
                line_dict[i] = test_dict
                num_adjcent_stars.append(test_dict)    

print()
print(f"Part 1: Sum Sym Adj: {sum([int(x) for x in sym_adj_numbers])}")
print(f"Part 2: Gear Ratio Sum: {sum([x['gear_ratio'] for x in num_adjcent_stars])}")
