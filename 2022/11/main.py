from collections import defaultdict
import heapq

def get_lines(path):
    with open(path) as f:
        return f.read().splitlines()
    
def save_monkey(monkeys, monkey):
    monkeys.append(monkey)

def get_empty_monkey():
    return {
        'items': None,
        'operation': None,
        'operation_val': None,
        'test' : None,
        'true' : None,
        'false': None
    }

def inspect_item(worry_level, monkey):
    operation = monkey['operation']
    val = monkey['operation_val']
    if operation == 'multiply':
        return worry_level * val
    elif operation == 'add':
        return worry_level + val
    else:
        return worry_level * worry_level
    
def throw_item(worry_level, monkeys, monkey):
    if worry_level % monkey['test'] == 0:
        monkeys[monkey['true']]['items'].append(worry_level)
    else:
        monkeys[monkey['false']]['items'].append(worry_level)

def process_monkey(data, monkey):
    if data == []: return
    if data[0] == 'Starting':
        tmp = []
        for i in range(2, len(data)):
            tmp.append(int(data[i].replace(',', '')))
        monkey['items'] = tmp
    elif data[0] == 'Operation:':
        if data[4] == '*':
            monkey['operation'] = 'multiply'
        else:
            monkey['operation'] = 'add'
        if data[5] == 'old':
            monkey['operation'] = 'square'
        else:
            monkey['operation_val'] = int(data[5])
    elif data[0] == 'Test:':
        monkey['test'] = int(data[3])
    elif data[1] == 'true:' or data[1] == 'false:':
        monkey[data[1].replace(':', '')] = int(data[5])

def bore_monkey(worry_level):
    return worry_level // 3

def count_inspection(key, dict):
    dict[key] += 1

def get_monkey_business(count_dict):
    largest = heapq.nlargest(2, count_dict.values())
    return largest[0] * largest[1]

def main():
    lines = get_lines('input.txt')
    monkeys = []
    new_monkey = get_empty_monkey()

    for line in lines:
        should_save_monkey = line[0:6] == 'Monkey' and line[0:8] != 'Monkey 0'
        if should_save_monkey:
            save_monkey(monkeys, new_monkey)
            new_monkey = get_empty_monkey()
        else:
            process_monkey(line.split(), new_monkey)
    save_monkey(monkeys, new_monkey)

    inspect_count = defaultdict(int)
    
    for rounds in range(20):
        for idx, monkey in enumerate(monkeys):
            for monkey_item in monkey['items']:
                count_inspection(idx, inspect_count)
                worry_level = monkey_item
                worry_level = inspect_item(worry_level, monkey)
                worry_level = bore_monkey(worry_level)
                throw_item(worry_level, monkeys, monkey)
            monkey['items'] = []

    print(f'Monkey_business: {get_monkey_business(inspect_count)}')

main()