"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""


# normal
def string_times(str, n):
    results = ""
    for i in range(n):
        results = results + str
    return results


# optimal
def string_times(str, n):
    return str * n


# test
if __name__ == "__main__":
    string_times("Hi", 2) == "HiHi"
    string_times("Hi", 3) == "HiHiHi"
    string_times("Hi", 1) == "Hi"
    string_times("Hi", 0) == ""
    string_times("Hi", 5) == "HiHiHiHiHi"
    string_times("Oh Boy!", 2) == "Oh Boy!Oh Boy!"
    string_times("x", 4) == "xxxx"
    string_times("", 4) == ""
    string_times("code", 2) == "codecode"
    string_times("code", 3) == "codecodecode"
