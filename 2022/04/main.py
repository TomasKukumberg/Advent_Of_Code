def get_list(path):
    with open(path) as f:
        return f.read().splitlines()

def get_separated_pairs(pairs):
    return pairs.split(',')

def get_min_max(pair):
    _min, _max = pair.split('-')
    return int(_min), int(_max)

def do_pairs_overlap(pairs):
    first_pair_min, first_pair_max = get_min_max(pairs[0])
    second_pair_min, second_pair_max = get_min_max(pairs[1])
    first_list = list(range(first_pair_min, first_pair_max + 1))
    second_list = list(range(second_pair_min, second_pair_max + 1))
    pairs_overlap = (set(first_list).issubset(set(second_list))) or (set(second_list).issubset(set(first_list)))
    return pairs_overlap

lst = get_list('input.txt')
total_overlaps = 0
for pair in lst:
    separated_pairs = get_separated_pairs(pair) 
    if do_pairs_overlap(separated_pairs):
        total_overlaps += 1
print(total_overlaps)