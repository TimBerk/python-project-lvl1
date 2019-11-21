# -*- coding:utf-8 -*-
from random import randint
import prompt


MIN_NUM = 1
MAX_NUM = 100
RULE = "Answer \"yes\" if number even otherwise answer \"no\"."


def start_game():
    num = randint(MIN_NUM, MAX_NUM)
    print("Question: " + str(num))
    answer = prompt.string('Answer: ')
    correct = "no" if num % 2 else "yes"
    return answer, correct
