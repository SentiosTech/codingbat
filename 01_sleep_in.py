"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""


# normal
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# compact
def sleep_in(weekday, vacation):
    return True if not weekday or vacation else False


# optimal
def sleep_in(weekday, vacation):
    return not weekday or vacation


# test
if __name__ == "__main__":
    sleep_in(False, False) == True
    sleep_in(True, False) == False
    sleep_in(False, True) == True
    sleep_in(True, True) == True
    print("✅ All tests passed!")
