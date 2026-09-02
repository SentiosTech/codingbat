"""
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""


# normal
def extra_end(str):
    last_two = str[-2:]
    return last_two * 3


# optimal
def extra_end(str):
    return str[:-2] * 3


# test
if __name__ == "__main__":
    extra_end("Hello") == "lololo"
extra_end("ab") == "ababab"
extra_end("Hi") == "HiHiHi"
extra_end("Candy") == "dydydy"
extra_end("Code") == "dedede"
