"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""


# normal
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i : i + 3] == [1, 2, 3]:
            return True
    return False


# optimal
def array123(nums):
    return [1, 2, 3] in [nums[i : i + 3] for i in range(len(nums) - 2)]


# test
if __name__ == "__main__":
    array123([1, 1, 2, 3, 1]) == True
    array123([1, 1, 2, 4, 1]) == False
    array123([1, 1, 2, 1, 2, 3]) == True
    array123([1, 1, 2, 1, 2, 1]) == False
    array123([1, 2, 3, 1, 2, 3]) == True
    array123([1, 2, 3]) == True
    array123([1, 1, 1]) == False
    array123([1, 2]) == False
    array123([1]) == False
    array123([]) == False
