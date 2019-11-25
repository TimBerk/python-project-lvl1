# -*- coding:utf-8 -*-
from brain_games.cli import greet, get_answer

MAX_ATTEMPT = 3


def start_game(name_player, game):

    count = 0

    while(count < MAX_ATTEMPT):

        quest, correct = game.question()
        answer = get_answer(quest)

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name_player}!")
            break

        print("Correct!")
        count += 1

    if count == MAX_ATTEMPT:
        print(f"Congratulations, {name_player}!")


def run(game):
    name_player = greet(game.RULE)

    if hasattr(game, 'question'):
        start_game(name_player, game)
