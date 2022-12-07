from random import randint
from random import choice

OPS = '+-*'


def game_logic():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    op = choice(OPS)
    question = f'{random_number_1} {op} {random_number_2}'
    answer = eval(question)
    return question, answer


DESC = 'What is the result of the expression?'
