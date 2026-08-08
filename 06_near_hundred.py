"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""


# normal
def near_hundred(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False


# compact
def near_hundred(n):
    cerca_100 = abs(n - 100) <= 10
    cerca_200 = abs(n - 200) <= 10
    return cerca_100 or cerca_200


# optimal
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


# test
if __name__ == "__main__":
    near_hundred(93) == True
    near_hundred(90) == True
    near_hundred(89) == False
    near_hundred(110) == True
    near_hundred(111) == False
    near_hundred(121) == False
    near_hundred(-101) == False
    near_hundred(-209) == False
    near_hundred(190) == True
    near_hundred(209) == True
    near_hundred(0) == False
    near_hundred(5) == False
    near_hundred(-50) == False
    near_hundred(191) == True
    near_hundred(189) == False
    near_hundred(200) == True
    near_hundred(210) == True
    near_hundred(211) == False
    near_hundred(290) == False
