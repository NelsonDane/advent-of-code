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
            #print(child.name)
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
                        # Make string
                        temp = ' '.join(temp)
                        file = Node(temp, parent=current_dir)

# Count duplicates and remove their sizes
to_delete = []
for pre, fill, node in RenderTree(top):
    if node.name != '':
        if is_folder(node.name):
            for i in range(len(node.children)):
                for j in range(len(node.children)):
                    if i != j:
                        child = node.children[i]
                        child2 = node.children[j]
                        if child.name == child2.name:
                            # Append to to_delete
                            to_delete.append(child)

# Remove duplicates from to_delete
delete = []
for i in to_delete:
    # Compare as strings but append as nodes
    if str(i) not in str(delete):
        delete.append(i)

# Remove duplicates (for the last time)
for i in delete:
    print(f'Removed {i.name} from {i.parent.name}')
    i.parent = None
                            
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
            dir_sizes.append(current_dir_size)
            if current_dir_size < 100000:
                below_100k += 1
                below_100k_size += current_dir_size
        else:
            temp = node.name.split(' ')[1]
            total_size += int(temp)

# Print tree
print('Final tree:')
for pre, fill, node in RenderTree(top):
    print("%s%s" % (pre, node.name))

# Print sizes
print(f'Part 1: {below_100k_size}')
print(f'Total size of disk: {total_size}')

# Part 2

# System Constants
SYSTEM_SIZE = 70000000
NEEDED_SPACE = 30000000

# Get disk free
disk_free = SYSTEM_SIZE - total_size
print(f'Disk free: {disk_free}')

# Needed for update
needed = NEEDED_SPACE - disk_free
print(f'Needed for update: {needed}')

# Get directories that could be deleted
possible_delete_dirs = []
for i in dir_sizes:
    if i >= needed:
        possible_delete_dirs.append(i)

# Get smallest directory in possible delete dirs
smallest = min(possible_delete_dirs)

# Print answers
print(f'Part 2: {smallest}')
