def getCommonBitInCol(arr, idx, arg):
    zeroes = ones = 0
    
    for el in arr:
        if el[idx] == '0':
            zeroes += 1
        else:
            ones += 1
    
    if arg == 'most':
        return '1' if zeroes > ones else '0'
    else:
        return '0' if zeroes > ones else '1' 


def removeAllInvalidRows(arr, most, idx):
    arr2 = arr.copy()
    for row in arr:
        if row[idx] != most and len(arr) > 1:
            arr2.remove(row)
    return arr2


with open("input.txt") as f:
    lines = f.read().splitlines()
    lines2 = lines.copy()

    for i in range(0, 12):
        most = getCommonBitInCol(lines, i, 'most')
        lines = removeAllInvalidRows(lines, most, i)

    for i in range(0, 12):
        least = getCommonBitInCol(lines2, i, 'least')
        lines2 = removeAllInvalidRows(lines2, least, i)
    
    print(f'Life support rating of the submarine is {int(lines[0], 2) * int(lines2[0], 2)}')