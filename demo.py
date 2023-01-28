var = "HeLlo World I Am ZiYa"

spilited_word = var.split(" ")


def reverse_words_order_and_swap_cases(sentence):
    spilited_word_list = sentence.split(" ")
    reverse_ord_swap_cases_worerd = ""
    i = len(spilited_word) - 1
    for word in spilited_word_list:
        swap_cases_word = ""
        for leter in spilited_word_list[i]:
            if leter.upper() == leter:
                leter = leter.lower()
            else:
                leter = leter.upper()
            swap_cases_word += leter

        reverse_ord_swap_cases_worerd = (
            reverse_ord_swap_cases_worerd + " " + swap_cases_word
        )
        i -= 1

    print(reverse_ord_swap_cases_worerd)


reverse_words_order_and_swap_cases("HeLlo World I Am ZiYa")

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    length = len(s)
    mod = n % length
    reapeat_times = int(n / length)
    # print(mod, reapeat_times)
    a_in_s = 0
    for i in s:
        if i == "a":
            a_in_s += 1

    result = reapeat_times * a_in_s
    if mod != 0:
        for j in s[0:mod]:
            if j == "a":
                result += 1

    print(result)


# repeatedString("aba", 10)
