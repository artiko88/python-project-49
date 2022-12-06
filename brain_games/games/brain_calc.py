#!/usr/bin/env python3
from brain_games.scripts.compare import run
from random import randint
from random import choice


def game_logic():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    ops = '+-*'
    op = choice(ops)
    question = f'{number1} {op} {number2}'
    answer = eval(question)
    return question, answer


def main():
    run(game_logic)


if __name__ == '__main__':
    main()
