def get_rucksacks(path):
    with open(path) as f:
        return f.read().splitlines()

def get_groups(rucksacks):
    groups = []
    for i in range(0, len(rucksacks) , 3):
        groups.append(rucksacks[i:i+3])
    return groups

def get_shared_item(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item

def get_item_priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - 96
    elif item >= 'A' and item <= 'Z':
        return ord(item) - 38

rucksacks = get_rucksacks('input.txt')
groups = get_groups(rucksacks)
total_sum_priority = 0
for group in groups:
    shared_item = get_shared_item(group)
    priority = get_item_priority(shared_item)
    total_sum_priority += priority
print(total_sum_priority)