# -*- coding:utf-8 -*-
from random import randint
import prompt


MIN_NUM = 1
MAX_NUM = 100
RULE = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def find_prime(a):
    b = 2
    while (a != b):
        if a % b:
            b += 1
        else:
            return "no"

    return "yes"


def question():
    num = randint(MIN_NUM, MAX_NUM)
    print(f"Question: {str(num)}")
    answer = prompt.string('Answer: ')
    correct = find_prime(num)
    return answer, correct
