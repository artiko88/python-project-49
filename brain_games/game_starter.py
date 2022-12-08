import prompt


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    correct_count = 0
    while correct_count < 3:
        question, r_ans = game.game_logic()
        print(f'Question: {question}')
        ans = prompt.string('Your answer:')
        if ans == str(r_ans):
            print('correct')
            correct_count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            return
        if correct_count == 3:
            print(f'Congratulations, {name}!')
