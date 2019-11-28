# -*- coding:utf-8 -*-
from math import sqrt
from random import randint


MIN_NUM = 1
MAX_NUM = 100
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_even(a):
    return not (a % 2)


def is_prime(n):
    if is_even(n):
        return False
    if n == 2:
        return True

    num = 3
    sqrt_n = sqrt(n)
    while num <= sqrt_n:
        if not n % num:
            return False
        num += 2
    return True


def question():
    num = randint(MIN_NUM, MAX_NUM)
    question = f"Question: {str(num)}"
    correct = "yes" if is_prime(num) else "no"
    return question, correct
