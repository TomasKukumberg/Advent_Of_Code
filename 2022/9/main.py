PLUS = 1
MINUS = 2

def get_turns(path):
    with open(path) as f:
        return f.read().splitlines()

def get_new_pos(pos1, pos2, operation):
    if operation == PLUS:
        return {"x" : pos1["x"] + pos2["x"], "y" : pos1["y"] + pos2["y"]}
    else:
        return {"x" : pos1["x"] - pos2["x"], "y" : pos1["y"] - pos2["y"]}

def move_head(head_pos, direction, unit):
    if direction == "L":
        return get_new_pos(head_pos, {"x" : unit, "y": 0}, MINUS)
    elif direction == "R":
        return get_new_pos(head_pos, {"x" : unit, "y" : 0}, PLUS)
    elif direction == "U":
        return get_new_pos(head_pos, {"x" : 0, "y" : unit}, MINUS)
    else:
        return get_new_pos(head_pos, {"x" : 0, "y": unit}, PLUS)

def move_tail(tail_pos, head_pos, direction):
    if direction == "L":
        return {"x" : head_pos["x"] + 1, "y" : tail_pos["y"]}
    elif direction == "R":
        return get_new_pos(head_pos, {"x" : unit, "y" : 0}, PLUS)
    elif direction == "U":
        return get_new_pos(head_pos, {"x" : 0, "y" : unit}, MINUS)
    else:
        return get_new_pos(head_pos, {"x" : 0, "y": unit}, PLUS)

turns = get_turns('input.txt')
head_pos = {"x" : 0, "y" : 0}
tail_pos = {"x" : 0, "y" : 0}
tail_visited = {}

for turn in turns:
    direction, unit = turn.split()
    head_pos = move_head(head_pos, direction, int(unit))
    tail_pos = move_tail(tail_pos, head_pos)
    print(f'direction : {direction} unit : {unit} head new position: {head_pos}')