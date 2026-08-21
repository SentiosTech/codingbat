"""
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""


# normal
def last2(str):
    results = 0
    for i in range(0, len(str) - 2):
        if str[i : i + 2] == str[-2:]:
            results += 1
    return results


# optimal
def last2(str):
    return len(
        [str[i : i + 2] for i in range(len(str) - 2) if str[i : i + 2] == str[-2:]]
    )


# test
if __name__ == "__main__":

    last2("hixxhi") == 1
    last2("xaxxaxaxx") == 1
    last2("axxxaaxx") == 2
    last2("xxaxxaxxaxx") == 3
    last2("xaxaxaxx") == 0
    last2("xxxx") == 2
    last2("13121312") == 1
    last2("11212") == 1
    last2("13121311") == 0
    last2("1717171") == 2
    last2("hi") == 0
    last2("h") == 0
    last2("") == 0
