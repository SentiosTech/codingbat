"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3)    'AbcAbcAbc'
"""


# normal
def front_times(str, n):
    if len(str) <= 3:
        return str * n
    else:
        return str[:3] * n


# optimal
def front_times(str, n):
    return str[:3] * n


# test
if __name__ == "__main__":
    front_times("Chocolate", 2) == "ChoCho"
    front_times("Chocolate", 3) == "ChoChoCho"
    front_times("Abc", 3) == "AbcAbcAbc"
    front_times("Ab", 4) == "AbAbAbAb"
    front_times("A", 4) == "AAAA"
    front_times("", 4) == ""
    front_times("Abc", 0) == ""
