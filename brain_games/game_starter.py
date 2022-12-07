import prompt


def get_name():
    global name
    name = prompt.string('May I have your name? ')
    return name


def greet():
    print("Welcome to the Brain Games!")
    name = get_name()
    print(f'Hello, {name}!')


def run(game, desc):
    greet()
    print(desc)
    correct_count = 0
    wrong_count = 0
    while correct_count < 3 and wrong_count == 0:
        question, r_ans = game()
        print(f'Question: {question}')
        ans = prompt.string('Your answer:')
        if ans == str(r_ans):
            print('correct')
            correct_count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            wrong_count += 1
        if correct_count == 3:
            print(f'Congratulations, {name}!')
