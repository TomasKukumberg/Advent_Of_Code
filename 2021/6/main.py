def simulateDay(fish):
    result = fish.copy()

    for idx, number in enumerate(fish):
        result[idx] = 6 if number == 0 else number - 1
        if number == 0:
            result.append(8)
    return result

with open('input.txt') as f:
    fish = f.read().split(',')
    fish = [ int(x) for x in fish ]
    
for i in range(80):
    fish = simulateDay(fish)

print(f'Fish count: {len(fish)}' )