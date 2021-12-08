from math import inf

def getFuelConsumption(numbers, moveTo):
    sum = 0
    for number in numbers:
        diff = abs(number - moveTo)
        sum += (diff + 1) * diff / 2 
    return (moveTo, int(sum))

with open('input.txt') as f:
    numbers = [int(x) for x in f.read().split(',')]

moveTo, min = -1, inf
max_num = max(numbers)

for i in range(max_num):
    tmp1, tmp2 = getFuelConsumption(numbers, i)
    if tmp2 < min:
        moveTo, min = tmp1, tmp2

print(f'Position {moveTo} will use the least fuel : {min}.')
