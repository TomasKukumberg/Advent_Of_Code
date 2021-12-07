def tst(numbers):
    result = numbers.copy()

    for idx, number in enumerate(numbers):
        result[idx] = 6 if number == 0 else number - 1
        if number == 0:
            result.append(8)
    return result

with open('input.txt') as f:
    numbers = f.read().split(',')
    numbers = [ int(x) for x in numbers ]
    
for i in range(80):
    numbers = tst(numbers)

print(len(numbers))