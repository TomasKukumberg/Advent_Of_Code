with open("input.txt") as f:
    cnt = 0
    lines = f.read().splitlines()
    for i in range(0, len(lines) - 2):
        num = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if i == 0:
            prev = num
        else:
            if num > prev:
                cnt += 1
            prev = num
    print(f"Higher count: {cnt}")