with open("input.txt") as f:
    pos = depth = aim = 0
    lines = f.readlines()
    
    for line in lines:
        line = line.replace('\n', '')
        direction, step = line.split()[0], int(line.split()[1])

        if direction == "forward":
            pos += step
            depth += aim * step
        elif direction == "up":
            aim -= step
        else:
            aim += step
    
    print(f"Final result: {pos * depth}")