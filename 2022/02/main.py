ENEMY_ROCK = 'A'
ENEMY_PAPER = 'B'
ENEMY_SCISSORS = 'C'
PLAYER_ROCK = 'X'
PLAYER_PAPER = 'Y'
PLAYER_SCISSORS = 'Z'

def get_rounds(path):
    with open(path) as f:
        return f.readlines()

def get_choice_score(player):
    choice_score = {PLAYER_ROCK : 1, PLAYER_PAPER : 2, PLAYER_SCISSORS : 3}
    return choice_score[player]

def get_result_score(enemy, player):
    wins = {ENEMY_ROCK : PLAYER_PAPER, ENEMY_PAPER : PLAYER_SCISSORS, ENEMY_SCISSORS : PLAYER_ROCK}
    draws = {ENEMY_ROCK : PLAYER_ROCK, ENEMY_PAPER : PLAYER_PAPER, ENEMY_SCISSORS : PLAYER_SCISSORS}
    if (enemy, player) in draws.items():
        return 3
    elif (enemy, player) in wins.items():
        return 6
    else:
        return 0

def get_score(enemy, player):
    return get_choice_score(player) + get_result_score(enemy, player)
            


rounds = get_rounds('input.txt')
total_score = 0
for round in rounds:
    enemy, player = round.split()
    total_score += get_score(enemy, player)
print(total_score)