from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def game_logic():
    random_number = randint(1, 100)
    if is_even(random_number):
        answer = 'yes'
    else:
        answer = 'no'
    return random_number, answer
