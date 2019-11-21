# -*- coding:utf-8 -*-
from random import randint
import prompt


MIN_NUM = 1
MAX_NUM = 50
RULE = "Find the greatest common divisor of given numbers."


def find_gcd(a, b):
    while (a != b):
        if a > b:
            a -= b
        else:
            b -= a

    return a


def question():
    num_1 = randint(MIN_NUM, MAX_NUM)
    num_2 = randint(MIN_NUM, MAX_NUM)
    print(f"Question: {str(num_1)} {str(num_2)}")
    answer = prompt.integer('Answer: ')
    correct = find_gcd(num_1, num_2)
    return answer, correct
