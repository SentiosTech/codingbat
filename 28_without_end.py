"""
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""


# normal
def without_end(str):
    value = str[1:-1]
    return value


# optimal
def without_end(str):
    return str[1:-1]


# test
if __name__ == "__main__":
    print(
        without_end("Hello") == "ell",
        without_end("java") == "av",
        without_end("coding") == "odin",
        without_end("code") == "od",
        without_end("ab") == "",
        without_end("Chocolate!") == "hocolate",
        without_end("kitten") == "itte",
        without_end("woohoo") == "ooho",
    )
