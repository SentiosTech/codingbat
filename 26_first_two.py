"""
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""


# normal
def first_two(str):
    if len(str) <= 2:
        return str
    else:
        return str[:2]


# optimal
def first_two(str):
    return str[:2]


# test
if __name__ == "__main__":
    first_two("Hello") == "He"
    first_two("abcdefg") == "ab"
    first_two("ab") == "ab"
    first_two("a") == "a"
    first_two("") == "" ""
    first_two("Kitten") == "Ki"
    first_two("hi") == "hi"
    first_two("hiya") == "hi"
