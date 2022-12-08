from random import randint

RULE = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 10)
    step = randint(1, 6)
    progression = list(range(start, 40, step))
    return progression


def game_logic():
    progression = generate_progression()
    random_index = randint(0, len(progression) - 1)
    answer = progression[random_index]
    progression[random_index] = '..'
    question = ''
    for i in range(0, len(progression)):
        question += str(progression[i])
        question += ' '
    return question, answer
