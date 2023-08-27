def get_map(path):
    with open(path) as f:
        return f.read().splitlines()

def is_visible(_map, row_idx, tree_idx):
    return (is_visible_left(_map, row_idx, tree_idx) 
            or is_visible_top(_map, row_idx, tree_idx) 
            or is_visible_right(_map, row_idx, tree_idx) 
            or is_visible_bottom(_map, row_idx, tree_idx))

def is_visible_top(_map, row_idx, tree_idx):
    tree_height = int(_map[row_idx][tree_idx])
    for _row_idx in range(row_idx):
        if int(_map[_row_idx][tree_idx]) >= tree_height:
            return False
    return True

def is_visible_bottom(_map, row_idx, tree_idx):
    tree_height = int(_map[row_idx][tree_idx])
    for _row_idx in range(row_idx + 1, len(_map)):
        if int(_map[_row_idx][tree_idx]) >= tree_height:
            return False
    return True

def is_visible_left(_map, row_idx, tree_idx):
    tree_height = int(_map[row_idx][tree_idx])
    for _tree_idx in range(tree_idx):
        if int(_map[row_idx][_tree_idx]) >= tree_height:
            return False
    return True

def is_visible_right(_map, row_idx, tree_idx):
    tree_height = int(_map[row_idx][tree_idx])
    for _tree_idx in range(tree_idx + 1, len(_map[0])):
        if int(_map[row_idx][_tree_idx]) >= tree_height:
            return False
    return True

_map = get_map('input.txt')

count = 0
for row_idx, row in enumerate(_map):
    for tree_idx, tree in enumerate(row):
        if is_visible(_map, row_idx, tree_idx):
            count += 1
print(count)