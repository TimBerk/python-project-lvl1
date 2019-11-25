# -*- coding:utf-8 -*-
from random import randint
import prompt


MIN_NUM = 1
MAX_NUM = 100
RULE = 'Answer "yes" if number even otherwise answer "no".'


def question():
    num = randint(MIN_NUM, MAX_NUM)
    question = "Question: " + str(num)
    correct = "no" if num % 2 else "yes"
    return question, correct
