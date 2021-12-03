with open("input.txt") as f:
    pos = depth = 0
    lines = f.read().splitlines()
    
    for line in lines:
        direction, step = line.split()[0], int(line.split()[1])

        if direction == "forward":
            pos += step
        elif direction == "up":
            depth -= step
        else:
            depth += step
    
    print(f"Final result: {pos * depth}")