# Nelson Dane
# Advent of Code 2022 Day 7

from anytree import Node, RenderTree

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1

# Check if string is a folder (folders don't have numbers)
def is_folder(string):
    for i in string:
        if i.isdigit():
            return False
    return True

# Get size of folder, recursively
def get_size(node):
    size = 0
    for child in node.children:
        if child.children:
            size += get_size(child)
        else:
            size += int(child.name.split(' ')[1])
    return size

# Create top node
top = current_dir = Node('')

# Loop through data
for i in range(len(data)):
    # Create file tree
    if data[i] != '$ cd /':
        if 'cd ' in data[i] and 'cd ..' not in data[i]:
            dir = data[i].split(' ')
            dir = Node(dir[2], parent=current_dir)
            current_dir = dir
        elif 'cd ..' in data[i]:
            current_dir = current_dir.parent
        elif 'ls' in data[i]:
            # Folder size
            dir_size = 0
            # Read all files until next command
            for j in range(i+1, len(data)):
                if '$' in data[j]:
                    break
                else:
                    if 'dir' not in data[j]:
                        # Swap size and name
                        temp = data[j].split(' ')
                        temp[0], temp[1] = temp[1], temp[0]
                        # Add size to total
                        dir_size += int(temp[1])
                        # Make string
                        temp = ' '.join(temp)
                        file = Node(temp, parent=current_dir)

# Sums
total_size = 0
parent_dir_size = 0
current_dir_size = 0

# Directories below 100k in size
below_100k = 0
below_100k_size = 0

# Current directory
dir_name = ''

# List of directory sizes
dir_sizes = []

# Traverse tree for sizes
for pre, fill, node in RenderTree(top):
    if node.name != '':
        if is_folder(node.name):
            dir_name = node.name
            current_dir_size = get_size(node)
            parent = node.parent
            if parent is None:
                parent_dir_size = current_dir_size
            else:
                parent_dir_size = get_size(node.parent)
            total_size += current_dir_size
            print(f'{dir_name} size: {current_dir_size}')
            dir_sizes.append(current_dir_size)
            if current_dir_size < 100000:
                below_100k += 1
                below_100k_size += current_dir_size

# Print sizes
print(f'Total size of disk: {parent_dir_size}')
print(f'{below_100k} directories below 100k, size: {below_100k_size}')

# Print tree
print('Final tree:')
for pre, fill, node in RenderTree(top):
    print("%s%s" % (pre, node.name))

# Part 2

# print(dir_sizes)
# System Constants
SYSTEM_SIZE = 70000000
NEEDED_SPACE = 30000000

# Get disk used
disk_used = parent_dir_size
print(f'Disk used: {disk_used}')

# Get disk free
disk_free = SYSTEM_SIZE - disk_used
print(f'Disk free: {disk_free}')

# Needed for update
needed = NEEDED_SPACE - disk_free
print(f'Needed for update: {needed}')

possible_delete_dirs = []

for i in dir_sizes:
    if i > needed:
        possible_delete_dirs.append(i)

# Get smallest directory in possible delete dirs
smallest = min(possible_delete_dirs)

print(f'Smallest directory to delete: {smallest}')


