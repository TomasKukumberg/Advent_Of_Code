def get_map(path):
    with open(path) as f:
        return f.read().splitlines()

def is_visible_custom(row_idx, tree_idx, _map, start, end, axis):
    tree_height = int(_map[row_idx][tree_idx])
    for idx in range(start, end):
        if axis == 'horizontal':
            if int(_map[row_idx][idx]) >= tree_height:
                return False
        else:
            if int(_map[idx][tree_idx]) >= tree_height:
                return False
    return True

def is_visible(_map, row_idx, tree_idx):
    left = is_visible_custom(row_idx, tree_idx, _map, 0, tree_idx, 'horizontal')
    top = is_visible_custom(row_idx, tree_idx, _map, 0, row_idx, 'vertical')
    right = is_visible_custom(row_idx, tree_idx, _map, tree_idx + 1, len(_map[0]), 'horizontal')
    bottom = is_visible_custom(row_idx, tree_idx, _map, row_idx + 1, len(_map), 'vertical')
    return left or top or right or bottom

_map = get_map('input.txt')

count = 0
for row_idx, row in enumerate(_map):
    for tree_idx, tree in enumerate(row):
        if is_visible(_map, row_idx, tree_idx):
            count += 1
print(count)