def get_rucksacks(path):
    with open(path) as f:
        return f.readlines()

def get_rucksack_compartments(rucksack):
    first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    return first, second

def get_shared_item(first, second):
    for item in first:
        if item in second:
            return item

def get_item_priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - 96
    elif item >= 'A' and item <= 'Z':
        return ord(item) - 38

rucksacks = get_rucksacks('input.txt')
sum_priorities = 0
for rucksack in rucksacks:
    first, second = get_rucksack_compartments(rucksack)
    shared_item = get_shared_item(first, second)
    priority = get_item_priority(shared_item)
    sum_priorities += priority
print(sum_priorities)