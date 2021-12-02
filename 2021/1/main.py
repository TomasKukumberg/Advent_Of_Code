with open("input.txt") as f:
    cnt = 0
    lines = f.readlines()
    for idx, line in enumerate(lines):
        line = int(line.replace('\n', ''))
        if idx == 0:
            prev = line
        else:
            if line > prev:
                cnt += 1
            prev = line
    print(f"Higher count: {cnt}")
