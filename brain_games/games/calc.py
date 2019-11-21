# -*- coding:utf-8 -*-
from random import randint, choice
import prompt


MIN_NUM = 1
MAX_NUM = 100
RULE = "What is the result of the expression?"
SIGNS = ["+", "-", "*"]


def start_game():
    num_1 = randint(MIN_NUM, MAX_NUM)
    num_2 = randint(MIN_NUM, MAX_NUM)
    sign = choice(SIGNS)
    print(f"Question: {str(num_1)} {sign} {str(num_2)}")
    answer = prompt.integer('Answer: ')

    if sign == "+":
        correct = num_1 + num_2
    elif sign == "-":
        correct = num_1 - num_2
    elif sign == "*":
        correct = num_1 * num_2

    return answer, correct
