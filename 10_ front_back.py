"""
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


# normal
def front_back(str):
    if len(str) == 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]


# compact
def front_back(str):
    egde_case = len(str) == 1
    if egde_case:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]


# optimal
def front_back(str):
    return str if len(str) == 1 else str[-1] + str[1:-1] + str[0]


# test
if __name__ == "__main__":
    front_back("code") == "eodc"
    front_back("a") == "a"
    front_back("ab") == "ba"
    front_back("abc") == "cba"
    front_back("") == ""
    front_back("Chocolate") == "ehocolatC"
    front_back("aavJ") == "Java"
    front_back("hello") == "oellh"
