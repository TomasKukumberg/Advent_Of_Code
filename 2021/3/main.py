with open("input.txt") as f:
    zeroDict = dict.fromkeys([x for x in range(12)], 0)
    oneDict = dict.fromkeys([x for x in range(12)], 0)
    lines = f.read().splitlines()
    
    for line in lines:
        for idx, el in enumerate(line):
            if el == '0': 
                zeroDict[idx] += 1
            else:
                oneDict[idx] += 1

    gamma = ""
    delta = ""
    
    for (k1,v1), (k2,v2) in zip(zeroDict.items(), oneDict.items()):
        if v1 > v2:
            gamma += "0"
            delta += "1"
        else:
            gamma += "1"
            delta += "0"
    
    gamma = int(gamma, 2)
    delta = int(delta, 2)
    
    print(f"Power consumption of the submarine is: {gamma * delta}")


        