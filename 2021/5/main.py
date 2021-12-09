with open('input.txt') as f:
    lines = f.read().split('\n')

points = {}
for line in lines:
    start, end = line.split('->')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    x1, x2, y1, y2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    
    if x1 == x2 or y1 == y2:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) not in points:
                    points[(x, y)] = 0
                points[(x, y)] += 1
    
sum = 0
for key in points:
    if points[key] > 1:
        sum += 1
print(f'Number of intersections: {sum}')