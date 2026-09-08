"""Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'"""


# optimal
def non_start(a, b):
    return a[1:] + b[1:]


# test
if __name__ == "__main__":
    non_start("Hello", "There") == "ellohere"
    non_start("java", "code") == "avaode"
    non_start("shotl", "java") == "hotlava"
    non_start("ab", "xy") == "by"
    non_start("ab", "x") == "b"
    non_start("x", "ac") == "c"
    non_start("a", "x") == ""
    non_start("kit", "kat") == "itat"
    non_start("mart", "dart") == "artart"
