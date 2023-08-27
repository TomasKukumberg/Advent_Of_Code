def get_output(path):
    with open(path) as f:
        return f.read().splitlines()

def is_command(line):
    return line[0] == '$'

def is_cd_command(line):
    return line[1] == 'cd'

def process_line(line):
    return line.split()

def is_dir(line):
    return line[0] == 'dir'

def change_dir(line, current_dir):
    if line[2] == "..":
        current_dir.pop(len(current_dir) - 1)
    else:
        if line[2] != "/":
            current_dir.append(line[2])

def save_file_size_to_dict(key, all_dirs, file_size):
    if key in all_dirs:
        all_dirs[key] += file_size
    else:
        all_dirs[key] = file_size

def save_file_size(current_dir, all_dirs, file_size):
    tmp = "/"
    save_file_size_to_dict(tmp, all_dirs, file_size)
    for entry in current_dir:
        tmp += entry + '/'
        save_file_size_to_dict(tmp, all_dirs, file_size)
    return tmp

def get_sum_of_dirs(all_dirs):
    _sum = 0
    for value in all_dirs.values():
        if value <= 100_000:
            _sum += value
    return _sum

output = get_output('input.txt')
current_dir = []
all_dirs = {}

for line in output:
    processed_line = process_line(line)
    if is_command(processed_line):
        if is_cd_command(processed_line):
            change_dir(processed_line, current_dir)
    else:
        if not is_dir(processed_line):
            save_file_size(current_dir, all_dirs, int(processed_line[0]))

_sum = get_sum_of_dirs(all_dirs)
print(_sum)