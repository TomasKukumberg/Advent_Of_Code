import math

def get_map(path):
    with open(path) as f:
        return f.read().splitlines()

def get_visibility(_map, row_idx, tree_idx):
    left = get_visibility_left(_map, row_idx, tree_idx)
    right = get_visibility_right(_map, row_idx, tree_idx)
    top = get_visibility_top(_map, row_idx, tree_idx)
    bottom = get_visibility_bottom(_map, row_idx, tree_idx)
    return left * right * top * bottom 

def get_visibility_top(_map, row_idx, tree_idx):
    count = 0
    tree_height = int(_map[row_idx][tree_idx])
    for _row_idx in range(row_idx - 1, -1, -1):
        if int(_map[_row_idx][tree_idx]) >= tree_height:
            return count + 1
        else:
            count += 1
    return count

def get_visibility_bottom(_map, row_idx, tree_idx):
    count = 0
    tree_height = int(_map[row_idx][tree_idx])
    for _row_idx in range(row_idx + 1, len(_map)):
        if int(_map[_row_idx][tree_idx]) >= tree_height:
            return count + 1
        else:
            count += 1
    return count

def get_visibility_left(_map, row_idx, tree_idx):
    count = 0
    tree_height = int(_map[row_idx][tree_idx]) 
    for _tree_idx in range(tree_idx - 1, -1, -1):
        if int(_map[row_idx][_tree_idx]) >= tree_height:
            return count + 1
        else:
            count += 1
    return count

def get_visibility_right(_map, row_idx, tree_idx):
    count = 0
    tree_height = int(_map[row_idx][tree_idx])
    for _tree_idx in range(tree_idx + 1, len(_map[0])):
        if int(_map[row_idx][_tree_idx]) >= tree_height:
            return count + 1
        else:
            count += 1
    return count

_map = get_map('input.txt')

max_visibility = -math.inf
for row_idx, row in enumerate(_map):
    for tree_idx, tree in enumerate(row):
        visibility = get_visibility(_map, row_idx, tree_idx)
        if visibility > max_visibility:
            max_visibility = visibility
print(max_visibility)