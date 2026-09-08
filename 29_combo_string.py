"""Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'"""


# normal
def combo_string(a, b):  # type: ignore
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


# optimal
def combo_string(a, b):
    return b + a + b if len(a) > len(b) else a + b + a


# test
if __name__ == "__main__":
    combo_string("Hello", "hi") == "hiHellohi"  # type: ignore
    combo_string("hi", "Hello") == "hiHellohi"
    combo_string("aaa", "b") == "baaab"
    combo_string("b", "aaa") == "baaab"
    combo_string("aaa", "") == "aaa"
    combo_string("", "bb") == "bb"
    combo_string("aaa", "1234") == "aaa1234aaa"
    combo_string("aaa", "bb") == "bbaaabb"
    combo_string("a", "bb") == "abba"
    combo_string("bb", "a") == "abba"
    combo_string("xyz", "ab") == "abxyzab"
