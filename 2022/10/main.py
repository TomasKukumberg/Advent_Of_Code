def get_lines(path):
    with open(path) as f:
        return f.read().splitlines()
    
def get_turns(lines):
    turns = []
    for line in lines:
        direction, distance = line.split()
        turns.append([direction, int(distance)])
    return turns

def move_head(direction, positions):
    if direction == 'U':
        positions['head'][1] += 1 
    elif direction == 'D':
        positions['head'][1] -= 1
    elif direction == 'L':
        positions['head'][0] -= 1
    else:
        positions['head'][0] += 1

def points_not_touching(positions):
    head = positions['head']
    tail = positions['tail']
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    
    if dx == 0 and dy == 0: # same position
        return False
    elif dx == 0 and abs(dy) == 1: # above or below each other
        return False
    elif abs(dx) == 1 and dy == 0: # next to each other
        return False
    elif abs(dx) == 1 and abs(dy) == 1: # diagonal to each other
        return False
    else:
        return True

def move_tail(positions):
    head = positions['head'] # ending position
    tail = positions['tail'] # starting position
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if  dx < 0 and dy == 0: # head is on the left side from the tail
        tail[0] -= 1
    elif dx > 0 and dy == 0: # head is on the right side from the tail
        tail[0] += 1
    elif dx == 0 and dy > 0: # head is above the tail
        tail[1] += 1
    elif dx == 0 and dy < 0: # head is below the tail
        tail[1] -= 1
    elif dx > 0 and dy > 0: # head is diagonally up and to the right of the tail
        tail[0] += 1
        tail[1] += 1
    elif dx > 0 and dy < 0: # head is diagonally down and to the right of the tail
        tail[0] += 1
        tail[1] -= 1
    elif dx < 0 and dy > 0: # head is diagonally up and to the left of the tail
        tail[0] -= 1
        tail[1] += 1
    elif dx < 0 and dy < 0: # head is diagonally down and to the left of the tail
        tail[0] -= 1
        tail[1] -= 1

def save_tail_position(positions):
    positions['visited'].add(tuple(positions['tail']))
    
def move(turn, positions):
    direction, distance = turn
    for i in range(distance):
        move_head(direction, positions)
        if points_not_touching(positions):
            move_tail(positions)
            save_tail_position(positions)

    
lines = get_lines('input.txt')
turns = get_turns(lines)

positions = {
    "head" : [0, 0],
    "tail" : [0, 0],
    "visited" : set((0, 0))
}

for turn in turns:
    move(turn, positions)

print(f'Total visited positions of tail: {len(positions["visited"])}')