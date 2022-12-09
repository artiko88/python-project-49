from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:  # Negative numbers can't be prime
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def game_logic():
    question = randint(1, 500)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
