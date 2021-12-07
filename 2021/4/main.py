def userWon(boards, dict):
    cnt = 0
    for idx, board in enumerate(boards):
        #if any row wins
        for cnt in range(0, 25, 5):
            if (idx,cnt) in dict and (idx, cnt + 1) in dict and (idx, cnt + 2) in dict and (idx, cnt + 3) in dict and (idx, cnt + 4) in dict:
                return True, idx
        #if any col wins
        for cnt in range(0, 5):
            if (idx,cnt) in dict and (idx, cnt + 5) in dict and (idx, cnt + 10) in dict and (idx, cnt + 15) in dict and (idx, cnt + 20) in dict:
                return True, idx
    return False, 0


def markNumber(boards, number, dict):
    for idx, board in enumerate(boards):
        for jdx, num in enumerate(board):
            if num == number:
                dict.add((idx, jdx))


def flatten(arr):
    result = []
    for idx, board in enumerate(arr):
        tmp = []
        for jdx, row in enumerate(board):
            tmp += row
        result.append(tmp)
    return result


def arrToInt(arr):
    for idx, board in enumerate(arr):
        for jdx, num in enumerate(board):
            arr[idx][jdx] = int(arr[idx][jdx])


def getFinalResult(boards, i, dict, number):
    sum = 0
    for idx, board in enumerate(boards):
        for jdx, num in enumerate(board):
            if (idx, jdx) not in dict and idx == i:
                sum += num
    return sum * number


with open("input.txt") as f:
    lines = f.read().splitlines()
    numbers = lines[0].split(',')
    numbers = [int(x) for x in numbers]
    bds = lines[2:]
    result = []
    tmp = []
    
    for line in bds:
        if line != '':
            nums = line.split()
            tmp.append(nums)
        else:
            result.append(tmp)
            tmp = []
    
    boards = flatten(result)
    arrToInt(boards)
    dict = set()
    
    for number in numbers:
        print(f'drawn number: {number}')
        markNumber(boards, number, dict)
        won, i = userWon(boards, dict)
        if won:
            print(f'User {i} has won with number {number}!')
            result = getFinalResult(boards, i, dict, number)
            print(f'result: {result}')
            break