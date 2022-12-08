from random import randint
from random import choice

RULE = 'What is the result of the expression?'
OPERATORS = '+-*'
ALLOWED_CHARS = "0123456789+-* "


def safe_eval(string):
    for char in string:
        if char not in ALLOWED_CHARS:
            raise Exception("Unsafe eval")
    return eval(string, {"__builtins__": None}, {})


def game_logic():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    op = choice(OPERATORS)
    question = f'{random_number_1} {op} {random_number_2}'
    answer = safe_eval(question)
    return question, answer
