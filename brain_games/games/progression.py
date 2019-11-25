# -*- coding:utf-8 -*-
from random import randint, choice
import prompt


MIN_NUM = 1
MAX_NUM = 100
MIN_STEP = 1
MAX_STEP = 10
RULE = "What number is missing in the progression?"


def build_progression(start_num, end_num, step):
    list1 = list(range(start_num, end_num, step))
    correct = choice(list1)
    list2 = [str(x) if x != correct else "." for x in list1]
    return str(correct), " ".join(list2)


def question():
    start_num = randint(MIN_NUM, MAX_NUM)
    step = randint(MIN_STEP, MAX_STEP)
    end_num = start_num + step * 10
    correct, progression = build_progression(start_num, end_num, step)
    question = f"Question: {progression}"
    return question, correct
