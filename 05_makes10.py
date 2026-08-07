"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""


# normal
def makes10(a, b):
    if a + b == 10 or (a == 10 or b == 10):
        return True
    else:
        return False


# compact
def makes10(a, b):
    value = a + b == 10 or (a == 10 or b == 10)
    return value


# optimal
def makes10(a, b):
    return a + b == 10 or (a == 10 or b == 10)


# test
if __name__ == "__main__":
    makes10(9, 10) == True
    makes10(9, 9) == False
    makes10(1, 9) == True
    makes10(10, 1) == True
    makes10(10, 10) == True
    makes10(8, 2) == True
    makes10(8, 3) == False
    makes10(10, 42) == True
    makes10(12, -2) == True
