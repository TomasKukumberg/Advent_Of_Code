def getMostCommonBitInCol(arr, idx):
    zeroes = ones = 0
    for el in arr:
        if el[idx] == '0':
            zeroes += 1
        else:
            ones += 1
    return '0' if zeroes > ones else '1'

def getLeastCommonBitInCol(arr, idx):
    zeroes = ones = 0
    for el in arr:
        if el[idx] == '0':
            zeroes += 1
        else:
            ones += 1
    return '1' if zeroes > ones else '0'

def removeAllInvalidRows(arr, most, idx):
    arr2 = arr.copy()
    for row in arr:
        if row[idx] != most and len(arr) > 1:
            arr2.remove(row)
    return arr2




"""
determine most common col number, then remove all rows without this number. repeat until last element remains
"""

with open("input.txt") as f:
    lines = f.read().splitlines()
    lines2 = lines.copy()

    for i in range(0, 12):
        most = getMostCommonBitInCol(lines, i)
        lines = removeAllInvalidRows(lines, most, i)

    print(lines)

    for i in range(0, 12):
        most = getLeastCommonBitInCol(lines2, i)
        lines2 = removeAllInvalidRows(lines2, most, i)
    
    print(int(lines[0], 2) * int(lines2[0], 2))
    #print(lines2)