"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""


# normal
def string_splosion(str):
    results = ""
    for i in range(1, len(str) + 1):
        results += str[:i]
    return results


# optimal
def string_splosion(str):
    return "".join([str[:i] for i in range(1, len(str) + 1)])


# test
if __name__ == "__main__":
    string_splosion("Code") == "CCoCodCode"
    string_splosion("abc") == "aababc"
    string_splosion("ab") == "aab"
    string_splosion("x") == "x"
    string_splosion("fade") == "ffafadfade"
    string_splosion("There") == "TThTheTherThere"
    string_splosion("Kitten") == "KKiKitKittKitteKitten"
    string_splosion("Bye") == "BByBye"
    string_splosion("Good") == "GGoGooGood"
    string_splosion("Bad") == "BBaBad"
