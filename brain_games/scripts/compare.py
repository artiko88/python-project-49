#!/usr/bin/env python3
import prompt
import brain_games.cli


def compare(question, right_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer:')
    if answer == str(right_answer):
        print('Correct!')
        return 'correct'
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
        return 'wrong'


def run(game, desc):
    brain_games.cli.greet()
    print(desc)
    correct_count = 0
    wrong_count = 0
    while correct_count < 3 and wrong_count == 0:
        question, answer = game()
        if compare(question, answer) == 'correct':
            correct_count += 1
        else:
            wrong_count += 1
        if correct_count == 3:
            print(f'Congratulations, {brain_games.cli.name}')
