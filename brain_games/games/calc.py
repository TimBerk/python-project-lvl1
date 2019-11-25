# -*- coding:utf-8 -*-
from random import randint, choice
import operator


MIN_NUM = 1
MAX_NUM = 20
RULE = "What is the result of the expression?"
SIGNS = [
    ("+", operator.add), ("-", operator.sub), ("*", operator.mul)
]


def question():
    num_1 = randint(MIN_NUM, MAX_NUM)
    num_2 = randint(MIN_NUM, MAX_NUM)
    sign, function = choice(SIGNS)
    question = f"Question: {str(num_1)} {sign} {str(num_2)}"
    correct = str(function(num_1, num_2))
    return question, correct
