from random import randint


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
    for _ in range(0, len(progression)):
        question += str(progression[_])
        question += ' '
    return question, answer


DESC = 'What number is missing in the progression?'
