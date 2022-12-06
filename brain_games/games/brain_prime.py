#!/usr/bin/env python3
from brain_games.scripts.compare import run
from random import randint


def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 'no'
        else:
            return 'yes'
    # If the number is less than 1, its also not a prime number.
    else:
        return 'no'


def game_logic():
    n = randint(1, 500)
    answer = is_prime(n)
    question = n
    return question, answer


def main():
    desc = 'Answer "yes" if the number is prime, otherwise answer is "no".'
    run(game_logic, desc)


if __name__ == '__main__':
    main()
