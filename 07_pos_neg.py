"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""


# normal
def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return True
        else:
            return False


# compact
def pos_neg(a, b, negative):
    ambos_negativos = a < 0 and b < 0
    exactamente_uno_negativo = (a < 0) != (b < 0)

    if negative:
        return ambos_negativos
    else:
        return exactamente_uno_negativo


# optimal
def pos_neg(a, b, negative):
    return (a < 0 and b < 0) if negative else ((a < 0) != (b < 0))


# test
if __name__ == "__main__":
    pos_neg(1, -1, False) == True
    pos_neg(-1, 1, False) == True
    pos_neg(-4, -5, True) == True
    pos_neg(-4, -5, False) == False
    pos_neg(-4, 5, False) == True
    pos_neg(-4, 5, True) == False
    pos_neg(1, 1, False) == False
    pos_neg(-1, -1, False) == False
    pos_neg(1, -1, True) == False
    pos_neg(-1, 1, True) == False
    pos_neg(1, 1, True) == False
    pos_neg(-1, -1, True) == True
    pos_neg(-6, 6, False) == True
    pos_neg(-5, -6, False) == False
    pos_neg(-2, -1, False) == False
    pos_neg(1, 2, False) == False
    pos_neg(-5, 6, True) == False
    pos_neg(-5, -5, True) == True
