with open("input.txt") as f:
    cnt = 0
    lines = f.readlines()
    for i in range(0, len(lines) - 2):
        num = int(lines[i].replace('\n', '')) + int(lines[i + 1].replace('\n', '')) + int(lines[i + 2].replace('\n', ''))
        if i == 0:
            prev = num
        else:
            if num > prev:
                cnt += 1
            prev = num
    print(f"Higher count: {cnt}")