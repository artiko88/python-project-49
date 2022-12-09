from random import randint
from random import choice

RULE = 'What is the result of the expression?'
OPERATORS = '+-*'
ALLOWED_CHARS = "0123456789+-* "


def random_expression(num1, num2):
    random_operator = choice(OPERATORS)
    question = f'{num1} {random_operator} {num2}'
    if random_operator == '+':
        answer = num1 + num2
        return question, answer
    elif random_operator == '-':
        answer = num1 - num2
        return question, answer
    elif random_operator == '*':
        answer = num1 * num2
        return question, answer


def game_logic():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    question, answer = random_expression(random_number_1, random_number_2)
    return question, answer
