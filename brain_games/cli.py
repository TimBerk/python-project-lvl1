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


def start_game(name_player, game):

    count = 0

    while(count < MAX_ATTEMPT):
        answer, correct = game.question()
        if answer == correct:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name_player}!")
            break

    if count == MAX_ATTEMPT:
        print(f"Congratulations, {name_player}!")


def run(game):
    name_player = greet(game.RULE)

    if hasattr(game, 'question'):
        start_game(name_player, game)
