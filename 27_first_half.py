"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""


# normal
def first_half(str):
    half = str[: len(str) // 2]
    return half


# optimal
def first_half(str):
    return str[: len(str) // 2]


# test
if __name__ == "__main__":
    first_half("WooHoo") == "Woo"
    first_half("HelloThere") == "Hello"
    first_half("abcdef") == "abc"
    first_half("ab") == "a"
    first_half("") == ""
    first_half("0123456789") == "01234"
    first_half("kitten") == "kit"
