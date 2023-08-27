import math

def get_max_calories(calories):
    max_calories = -math.inf
    for calorie in calories:
        if calorie > max_calories:
            max_calories = calorie
    return max_calories

def get_calories(path):
    sum_tmp = 0
    calories = []
    with open(path) as f:
        for calorie in f.readlines():
            if calorie == "\n":
                calories.append(sum_tmp)
                sum_tmp = 0
            else:
                sum_tmp += int(calorie)
        return calories


calories = get_calories('input.txt')
max_calories = get_max_calories(calories)
print(max_calories)