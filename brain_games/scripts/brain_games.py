#!/usr/bin/env python3
import prompt


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def greet():
    print("Welcome to the Brain Games!")
    global name
    name = get_name()
    print(f'Hello, {name}!')


def main():
    greet()


if __name__ == '__main__':
    main()
