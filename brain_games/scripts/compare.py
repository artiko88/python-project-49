#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user, name


def compare(question, right_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer:')
    if answer == str(right_answer):
        print('Correct!')
        return 'correct'
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
        return 'wrong'


def run(game):
    welcome_user()
    correct_count = 0
    wrong_count = 0
    while correct_count < 3 and wrong_count == 0:
        question, answer = game()
        if compare(question, answer) == 'correct':
            correct_count += 1
        else:
            wrong_count += 1
        if correct_count == 3:
            print(f'Congratulations, {name}')
