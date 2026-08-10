"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""


# normal
def not_string(str):
    if str.startswith("not"):
        return str
    else:
        return "not" + " " + str


# compact
def not_string(str):
    already_not = str.startswith("not")
    if already_not:
        return str
    else:
        return "not " + str


# optimal
def not_string(str):
    return str if str.startswith("not") else "not" + " " + str


# test
if __name__ == "__main__":
    not_string("candy") == "not candy"
    not_string("x") == "not x"
    not_string("not bad") == "not bad"
    not_string("bad") == "not bad"
    not_string("not") == "not"
    not_string("is not") == "not is not"
    not_string("no") == "not no"
