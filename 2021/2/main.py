with open("input.txt") as f:
    pos = depth = 0
    lines = f.readlines()
    
    for line in lines:
        line = line.replace('\n', '')
        direction, step = line.split()[0], int(line.split()[1])

        if direction == "forward":
            pos += step
        elif direction == "up":
            depth -= step
        else:
            depth += step
    
    print(f"Final result: {pos * depth}")