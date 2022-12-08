from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_logic():
    question = randint(1, 100)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
