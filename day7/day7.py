# Nelson Dane
# Advent of Code 2022 Day 7

from anytree import Node, RenderTree

# Read in the input file
with open('practice.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1

# Create top node
top = current_dir = Node('')

# Loop through data
for i in range(len(data)):
    # Create file tree
    if data[i] != '$ cd /':
        if 'cd' in data[i] and 'cd ..' not in data[i]:
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

dir_name = ''

# Traverse tree for sizes
for pre, fill, node in RenderTree(top):
    parent = node.parent
    if node.name != '':
        old_name = dir_name
        #print(old_name)
        temp = node.name.split(' ')
        name = temp[0]
        try:
            # If it has a file size, it is a file
            size = int(temp[1])
        except:
            # If file fails, it is a directory
            size = 0
            current_dir_size = 0
            dir_name = name
        # Add to total
        total_size += size
        # Make sure parent is not root
        if dir_name != '':
            current_dir_size += size
        else:
            # Add to parent dir
            parent_dir_size += current_dir_size
            # Reset current dir
            current_dir_size = 0
        print(f'Size of {old_name}: {parent_dir_size}')
        print(f'Current dir size: {current_dir_size}')
        print(f'Total size: {total_size}')

print(f'Total size of {old_name}: {current_dir_size}')
# Print total size
print(f'Total size: {total_size}')

# Print tree
print('Final tree:')
for pre, fill, node in RenderTree(top):
    print("%s%s" % (pre, node.name))
