#!/usr/bin/env python3
from brain_games.scripts.compare import run
from random import randint


def game_logic():
    number = randint(1, 100)
    question = number
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def main():
    desc = 'Answer "yes" if the number is even, otherwise answer "no".'
    run(game_logic, desc)


if __name__ == '__main__':
    main()
