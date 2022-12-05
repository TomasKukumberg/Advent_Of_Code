def get_crates_and_arrangements(path):
    with open(path) as f:
        crates_and_arrangements = f.read().splitlines()
        crates, arrangements =  split_crates_and_arrangements(crates_and_arrangements)
        return crates, arrangements

def save_crate(crate_stacks, line):
    crate_positions = {1 : 1, 2 : 5, 3 : 9, 4: 13, 5 : 17, 6 : 21, 7 : 25, 8 : 29, 9 : 33}
    for key in crate_positions.keys():
        if line[crate_positions[key]] != ' ':
            crate_stacks[key].append(line[crate_positions[key]])

def get_arrangement(line):
    tmp = line.split()
    return [int(tmp[1]), int(tmp[3]), int(tmp[5])]

def split_crates_and_arrangements(crates_and_arrangements):
    crate_stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    arrangements = []
    separator = ' 1   2   3   4   5   6   7   8   9 '
    saving_arrangements = False
    for line in crates_and_arrangements:
        if line == '' or line == separator:
            saving_arrangements = True
        elif saving_arrangements:
            arrangement = get_arrangement(line)
            arrangements.append(arrangement)
        else:
            save_crate(crate_stacks, line)
    return crate_stacks, arrangements

def move_crates(crates, arrangements):
    for arrangement in arrangements:
        tmp = []
        for crate_quantity in range(arrangement[0]):
            tmp.insert(0, crates[arrangement[1]].pop(0))
        for t in tmp:
            crates[arrangement[2]].insert(0, t)

def get_message(stack):
    message = []
    for crates in stack.values():
        if crates:
            message.append(crates.pop(0))
    return message

crates, arrangements = get_crates_and_arrangements('input.txt')
move_crates(crates, arrangements)
message = get_message(crates)
print(''.join(message))