"""
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""


# normal
def make_abba(a, b):
    abba_result = a + b + b + a
    return abba_result


# optimal
def make_abba(a, b):
    return a + b + b + a


# test
if __name__ == "__main__":
    make_abba("Hi", "Bye") == "HiByeByeHi"
    make_abba("Yo", "Alice") == "YoAliceAliceYo"
    make_abba("What", "Up") == "WhatUpUpWhat"
    make_abba("aaa", "bbb") == "aaabbbbbbaaa"
    make_abba("x", "y") == "xyyx"
    make_abba("x", "") == "xx"
    make_abba("", "y") == "yy"
    make_abba("Bo", "Ya") == "BoYaYaBo"
    make_abba("Ya", "Ya") == "YaYaYaYa"
