def get_coms(path):
    with open(path) as f:
        tmp = "".join(f.read().splitlines())
        return [*tmp]

def is_marker(arr):
    return len(arr) == len(set(arr))

coms = get_coms('input.txt')
marker_index = None
window_size = 14

for i in range(len(coms)):
    if is_marker(coms[i:i+window_size]):
        marker_index = i + window_size
        break
    
print(marker_index)