from random import randint
from random import choice

RULE = 'What is the result of the expression?'
OPERATORS = '+-*'


def get_expression_result(num1, num2, random_operator):
    if random_operator == '+':
        answer = num1 + num2
        return answer
    elif random_operator == '-':
        answer = num1 - num2
        return answer
    elif random_operator == '*':
        answer = num1 * num2
        return answer


def game_logic():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    random_operator = choice(OPERATORS)
    question = f'{random_number_1} {random_operator} {random_number_2}'
    answer = random_expression(random_number_1,
                               random_number_2,
                               random_operator)
    return question, answer
