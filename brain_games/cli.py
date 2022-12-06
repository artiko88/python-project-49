import prompt


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def greet():
    print("Welcome to the Brain Games!")
    global name
    name = get_name()
    welcome_user()


def welcome_user():
    print(f'Hello, {name}!')
