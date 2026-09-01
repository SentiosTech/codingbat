"""
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
"""


# normal
def make_out_word(out, word):
    word_in_middle = f"{out[:2]}{word}{out[2:]}"
    return word_in_middle


# optimal
def make_out_word(out, word):
    return out[:2] + word + out[2:]


# test
if __name__ == "__main__":
    make_out_word("<<>>", "Yay") == "<<Yay>>"
    make_out_word("<<>>", "WooHoo") == "<<WooHoo>>"
    make_out_word("[[]]", "word") == "[[word]]"
    make_out_word("HHoo", "Hello") == "HHHellooo"
    make_out_word("abyz", "YAY") == "abYAYyz"
