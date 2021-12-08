def getFuelConsumption(numbers, moveTo):
    sum = 0
    for number in numbers:
        sum += abs(number - moveTo)
    return moveTo, sum

with open('input.txt') as f:
    numbers = [int(x) for x in f.read().split(',')]

moveTo, min = getFuelConsumption(numbers, numbers[0])

for i in range(1, len(numbers)):
    tmp1, tmp2 = getFuelConsumption(numbers, numbers[i])
    if tmp2 < min:
        moveTo, min = tmp1, tmp2

print(f'Position {moveTo} will use the least fuel : {min}.')

