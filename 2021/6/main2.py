from collections import defaultdict

with open('input.txt') as f:
    fish = f.read().split(',')
    fish = [ int(x) for x in fish ]

freq = defaultdict(int)

for i in fish:
    if i not in freq:
        freq[i] = 0
    freq[i] += 1

days = 256

for _ in range(days):
    new_freq = defaultdict(int)
    for k, cnt in freq.items():
        if k == 0:
            new_freq[6] += cnt
            new_freq[8] = cnt
        else:
            new_freq[k-1] += cnt
    freq = new_freq

print(sum(freq.values()))

