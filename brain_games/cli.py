# -*- coding:utf-8 -*-
import prompt


MAX_ATTEMPT = 3


def run(game=None):
    print()
    print("Welcome to the Brain Games!")
    if game is not None:
        print(game.RULE)
    print()

    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    if game is not None:
        print()
        count = 0

        while(count < MAX_ATTEMPT):
            answer, correct = game.start_game()
            if answer == correct:
                print("Correct!")
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. ",
                      f"Correct answer was '{correct}'.")
                break

        if count == MAX_ATTEMPT:
            print(f"Congratulations, {name}!")
        else:
            print(f"Let's try again, {name}!")
