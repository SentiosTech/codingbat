"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""


# normal
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


# compact
def parrot_trouble(talking, hour):
    variable = hour < 7 or hour > 20
    return talking and variable


# optimal
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


# test
if __name__ == "__main__":
    parrot_trouble(True, 6) == True
    parrot_trouble(True, 7) == False
    parrot_trouble(False, 6) == False
    parrot_trouble(True, 21) == True
    parrot_trouble(False, 21) == False
    parrot_trouble(False, 20) == False
    parrot_trouble(True, 23) == True
    parrot_trouble(False, 23) == False
    parrot_trouble(True, 20) == False
    parrot_trouble(False, 12) == False
