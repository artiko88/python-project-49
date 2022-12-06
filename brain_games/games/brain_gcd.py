#!/usr/bin/env python3
from brain_games.scripts.compare import run
from random import randint


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


def game_logic():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    answer = gcd(number1, number2)
    return question, answer


def main():
    desc = 'Find the greatest common divisor of given numbers.'
    run(game_logic, desc)


if __name__ == '__main__':
    main()
