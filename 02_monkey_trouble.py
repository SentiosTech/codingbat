"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""


# normal
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif a_smile or b_smile:
        return False
    else:
        return True


# compact
def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)


# optimal
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


# test
if __name__ == "__main__":
    monkey_trouble(True, True) == True
    monkey_trouble(False, False) == True
    monkey_trouble(True, False) == False
    monkey_trouble(False, True) == False
    print("✅ All tests passed!")
