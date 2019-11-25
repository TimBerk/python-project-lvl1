# -*- coding:utf-8 -*-
from random import randint


MIN_NUM = 1
MAX_NUM = 100
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_even(a):
    return False if a % 2 else True


def is_prime(n):
    if n <= 1 or is_even(n):
        return False
    if n == 2:
        return True

    num = 2
    while num ** 2 <= n:
        if n % num == 0:
            return False
        num += 1
    return True


def question():
    num = randint(MIN_NUM, MAX_NUM)
    question = f"Question: {str(num)}"
    correct = "yes" if is_prime(num) else "no"
    return question, correct
