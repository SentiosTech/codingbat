"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""


# normal
def string_bits(str):
    results = ""
    for i in range(0, len(str), 2):
        results += str[i]
    return results


# optimal
def string_bits(str):
    str[::2]


# test:
if __name__ == "__main__":
    string_bits("Hello") == "Hlo"
    string_bits("Hi") == "H"
    string_bits("Heeololeo") == "Hello"
    string_bits("HiHiHi") == "HHH"
    string_bits("") == ""
    string_bits("Greetings") == "Getns"
    string_bits("Chocoate") == "Coot"
    string_bits("pi") == "p"
    string_bits("Hello Kitten") == "HloKte"
    string_bits("hxaxpxpxy") == "happy"
