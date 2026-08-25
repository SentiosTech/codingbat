"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""


# normal
def array_front9(nums):
    if 9 in nums[:4]:
        return True
    else:
        return False


# optimal
def array_front9(nums):
    return 9 in nums[:4]


# test
if __name__ == "__main__":
    array_front9([1, 2, 9, 3, 4]) == True
    array_front9([1, 2, 3, 4, 9]) == False
    array_front9([1, 2, 3, 4, 5]) == False
    array_front9([9, 2, 3]) == True
    array_front9([1, 9, 9]) == True
    array_front9([1, 2, 3]) == False
    array_front9([1, 9]) == True
    array_front9([5, 5]) == False
    array_front9([2]) == False
    array_front9([9]) == True
    array_front9([]) == False
    array_front9([3, 9, 2, 3, 3]) == True
