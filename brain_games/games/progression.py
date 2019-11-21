# -*- coding:utf-8 -*-
from random import randint, choice
import prompt


MIN_NUM = 1
MAX_NUM = 100
MIN_STEP = 1
MAX_STEP = 10
RULE = "What number is missing in the progression?"


def build_progression(start_num, end_num, step):
    list_1 = [i for i in range(start_num, end_num, step)]
    correct = choice(list_1)
    k_val = list_1.index(correct)
    list_2 = [str(x) if key != k_val else "." for key, x in enumerate(list_1)]
    return correct, " ".join(list_2)


def question():
    start_num = randint(MIN_NUM, MAX_NUM)
    step = randint(MIN_STEP, MAX_STEP)
    end_num = start_num + step * 10
    correct, progression = build_progression(start_num, end_num, step)
    print(f"Question: {progression}")
    answer = prompt.integer('Answer: ')
    return answer, correct
