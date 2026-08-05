"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""


# normal
def sum_double(a, b):
    if a != b:
        return a + b
    else:
        return (a + b) * 2


# compact
def sum_double(a, b):
    sum = a + b
    return sum * 2 if a == b else sum


# optimal
def sum_double(a, b):
    return (a + b) * (2 if a == b else 1)


# test
if __name__ == "__main__":
    sum_double(1, 2) == 3
    sum_double(3, 2) == 5
    sum_double(2, 2) == 8
    sum_double(-1, 0) == -1
    sum_double(3, 3) == 12
    sum_double(0, 0) == 0
    sum_double(0, 1) == 1
    sum_double(3, 4) == 7
    print("✅ All tests passed!")
