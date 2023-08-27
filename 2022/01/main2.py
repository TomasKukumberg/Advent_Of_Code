import math

def sum_max_calories(max_calories):
    sum_max = 0
    for max_calorie in max_calories:
        sum_max += max_calorie
    return sum_max 

def get_max_calories(calories):
    max_calories_1, max_calories_2, max_calories_3 = -math.inf, -math.inf, -math.inf
    for calorie in calories:
        if calorie > max_calories_1:
            max_calories_3 = max_calories_2
            max_calories_2 = max_calories_1
            max_calories_1 = calorie
        elif calorie > max_calories_2:
            max_calories_3 = max_calories_2
            max_calories_2 = calorie
        elif calorie > max_calories_3:
            max_calories_3 = calorie
    return max_calories_1, max_calories_2, max_calories_3  

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
sum_max = sum_max_calories(max_calories) 
print(sum_max)