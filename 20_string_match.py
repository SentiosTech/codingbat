"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

"""


# normal
def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i : i + 2] == b[i : i + 2]:
            count += 1
    return count


# optimal
def string_match(a, b):
    return len(
        [
            a[i : i + 2]
            for i in range(min(len(a), len(b)) - 1)
            if a[i : i + 2] == b[i : i + 2]
        ]
    )


# test
if __name__ == "__main__":
    string_match("xxcaazz", "xxbaaz") == 3
    string_match("abc", "abc") == 2
    string_match("abc", "axc") == 0
    string_match("hello", "he") == 1
    string_match("he", "hello") == 1
    string_match("h", "hello") == 0
    string_match("", "hello") == 0
    string_match("aabbccdd", "abbbxxd") == 1
    string_match("aaxxaaxx", "iaxxai") == 3
    string_match("iaxxai", "aaxxaaxx") == 3
