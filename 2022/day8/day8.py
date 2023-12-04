# Nelson Dane
# Advent of Code 2022 Day 8

import sys
from colorama import Fore

# Get input args
filename = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'e':
    filename = 'example.txt'

# Read in the input file
with open(filename, 'r') as f:
    data = f.read().splitlines()

def print_tree_grid(tree_grid):
    for line_index, line in enumerate(data):
        for tree_index, tree in enumerate(line):
            tree_dict = next((tree for tree in tree_grid if tree['row'] == line_index and tree['col'] == tree_index), None)
            if tree_dict is not None:
                if tree_dict['visible']:
                    print(f"{Fore.GREEN}{tree}{Fore.RESET}", end='')
                else:
                    print(f"{Fore.RED}{tree}{Fore.RESET}", end='')
            else:
                print(f"{Fore.WHITE}{tree}{Fore.RESET}", end='')
        print()

def list_safe_get(list, index):
    if index < len(list):
        return list[index]
    else:
        return None

def trees_horizontal_dir(tree_index, line, direction):
    if direction == 'left':
        all_trees = line[:tree_index]
        tree_list = list(reversed(all_trees))
    elif direction == 'right':
        all_trees = line[tree_index+1:]
        tree_list = list(all_trees)
    if tree_list is None:
        return []
    return tree_list

def trees_vertical_dir(tree_index, line_index, data, direction):
    all_trees = []
    if direction == 'up':
        for i in range(0, line_index):
            all_trees.append(list_safe_get(data[i], tree_index))
        all_trees.reverse()
    elif direction == 'down':
        for i in range(line_index+1, len(data)):
            all_trees.append(list_safe_get(data[i], tree_index))
    return all_trees

def tree_is_visible(tree_value, trees_left, trees_right, trees_up, trees_down):
    visible_from_left = all(tree_value > tree for tree in trees_left)
    visible_from_right = all(tree_value > tree for tree in trees_right)
    visible_from_up = all(tree_value > tree for tree in trees_up)
    visible_from_down = all(tree_value > tree for tree in trees_down)
    is_visible = visible_from_left or visible_from_right or visible_from_up or visible_from_down
    return is_visible

def trees_before_blocked(tree_value, tree_list):
    unblocked_trees = []
    for tree in tree_list:
        unblocked_trees.append(tree)
        if tree_value <= tree:
            break
    return unblocked_trees

def tree_viewing_score(tree_value, trees_left, trees_right, trees_up, trees_down):
    # Amount of trees until it's blocked
    unblocked_trees_left = trees_before_blocked(tree_value, trees_left)
    unblocked_trees_right = trees_before_blocked(tree_value, trees_right)
    unblocked_trees_up = trees_before_blocked(tree_value, trees_up)
    unblocked_trees_down = trees_before_blocked(tree_value, trees_down)
    viewing_score = len(unblocked_trees_left) * len(unblocked_trees_right) * len(unblocked_trees_up) * len(unblocked_trees_down)
    return viewing_score

# Part 1
tree_grid = []
for line_index, line in enumerate(data):
    for tree_index, tree in enumerate(line):
        tree_dict = {
        'row': 0,
        'col': 0,
        'value': None,
        'visible': False,
        'viewing_score': 0
    }
        all_trees_left = trees_horizontal_dir(tree_index, line, 'left')
        all_trees_right = trees_horizontal_dir(tree_index, line, 'right')
        all_trees_up = trees_vertical_dir(tree_index, line_index, data, 'up')
        all_trees_down = trees_vertical_dir(tree_index, line_index, data, 'down')
        # print(f"Up: {all_trees_up}, Down: {all_trees_down}")
        # print(f"Left: {all_trees_left}, Right: {all_trees_right}")
        tree_dict['row'] = line_index
        tree_dict['col'] = tree_index
        tree_dict['value'] = tree
        tree_dict['visible'] = tree_is_visible(tree, all_trees_left, all_trees_right, all_trees_up, all_trees_down)
        tree_dict['viewing_score'] = tree_viewing_score(tree, all_trees_left, all_trees_right, all_trees_up, all_trees_down)
        tree_grid.append(tree_dict)

# print(f"Tree Grid: {tree_grid}")
print_tree_grid(tree_grid)
print(f"Trees Visible: {sum(tree['visible'] for tree in tree_grid)}")

# Part 2
print(f"Best Viewing Score: {max(tree['viewing_score'] for tree in tree_grid)}")
