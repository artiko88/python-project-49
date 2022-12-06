#!/usr/bin/env python3
from brain_games.scripts.compare import run
from random import randint


def game_logic():
    start = randint(1, 10)
    step = randint(1, 6)
    progression = list(range(start, 40, step))
    randindx = randint(0, len(progression) - 1)
    prog_question = progression.copy()
    prog_question[randindx] = '...'
    question = str()
    for _ in range(0, len(progression)):
        question += str(prog_question[_])
        question += ' '
    answer = progression[randindx]
    return question, answer


def main():
    desc = 'What number is missing in this progression?'
    run(game_logic, desc)


if __name__ == '__main__':
    main()
