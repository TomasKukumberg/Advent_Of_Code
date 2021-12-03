with open("input.txt") as f:
    pos = depth = aim = 0
    lines = f.read().splitlines()
    
    for line in lines:
        direction, step = line.split()[0], int(line.split()[1])

        if direction == "forward":
            pos += step
            depth += aim * step
        elif direction == "up":
            aim -= step
        else:
            aim += step
    
    print(f"Final result: {pos * depth}")