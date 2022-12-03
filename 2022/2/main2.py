ENEMY_ROCK = 'A'
ENEMY_PAPER = 'B'
ENEMY_SCISSORS = 'C'
PLAYER_ROCK = 1
PLAYER_PAPER = 2
PLAYER_SCISSORS = 3
RESULT_LOSE = 'X'
RESULT_DRAW = 'Y'
RESULT_WIN = 'Z'

def get_rounds(path):
    with open(path) as f:
        return f.readlines()

def get_player_choice(enemy, result):
    enemy_player_draw = {ENEMY_PAPER : PLAYER_PAPER, ENEMY_ROCK : PLAYER_ROCK, ENEMY_SCISSORS : PLAYER_SCISSORS}
    enemy_player_win = {ENEMY_PAPER : PLAYER_SCISSORS, ENEMY_ROCK : PLAYER_PAPER, ENEMY_SCISSORS : PLAYER_ROCK}
    enemy_player_lose = {ENEMY_PAPER : PLAYER_ROCK, ENEMY_ROCK : PLAYER_SCISSORS, ENEMY_SCISSORS : PLAYER_PAPER}
    if result == RESULT_DRAW:
        return  enemy_player_draw[enemy]
    elif result == RESULT_WIN:
        return enemy_player_win[enemy]
    else:
        return enemy_player_lose[enemy]

def get_choice_score(player):
    choices_points = {PLAYER_ROCK : 1, PLAYER_PAPER : 2, PLAYER_SCISSORS : 3}
    return choices_points[player]

def get_result_score(result):
    results = {RESULT_DRAW : 3, RESULT_WIN : 6, RESULT_LOSE : 0}
    return results[result]

def get_score(enemy, result):
    player = get_player_choice(enemy, result)
    return get_choice_score(player) + get_result_score(result)
            


rounds = get_rounds('input.txt')
total_score = 0
for round in rounds:
    enemy, result = round.split()
    total_score += get_score(enemy, result)
print(total_score)