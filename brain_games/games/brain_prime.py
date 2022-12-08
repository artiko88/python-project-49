from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    # If the number is less than 1, its also not a prime number.
    else:
        return False


def game_logic():
    question = randint(1, 500)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
