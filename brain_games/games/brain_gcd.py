from random import randint


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


def game_logic():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    question = f'{random_number_1} {random_number_2}'
    answer = gcd(random_number_1, random_number_2)
    return question, answer


DESC = 'Find the greatest common divisor of given numbers.'
