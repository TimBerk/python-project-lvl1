# -*- coding:utf-8 -*-
import prompt


MAX_ATTEMPT = 3


def greet(rules=None):

    print()
    print("Welcome to the Brain Games!")
    if rules is not None:
        print(rules)
    print()

    name_player = prompt.string('May I have your name? ')
    print(f"Hello, {name_player}!")
    print()

    return name_player


def get_answer(question):
    print(question)
    answer = prompt.string('Answer: ')
    return answer
