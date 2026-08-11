"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""


# normal
def missing_char(str, n):
    before_n = str[:n]
    after_n = str[n + 1 :]
    return before_n + after_n


# compact
def missing_char(str, n):
    before_n = str[:n]
    return before_n + str[n + 1 :]


# optimal
def missing_char(str, n):
    return str[:n] + str[n + 1 :]


# test
if __name__ == "__main__":
    missing_char("kitten", 1) == "ktten"
    missing_char("kitten", 0) == "itten"
    missing_char("kitten", 4) == "kittn"
    missing_char("Hi", 0) == "i"
    missing_char("Hi", 1) == "H"
    missing_char("code", 0) == "ode"
    missing_char("code", 1) == "cde"
    missing_char("code", 2) == "coe"
    missing_char("code", 3) == "cod"
    missing_char("chocolate", 8) == "chocolat"
