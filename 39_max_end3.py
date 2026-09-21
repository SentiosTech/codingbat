"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""


# normal
def max_end3(nums):
    return [max(nums[0], nums[-1])] * 3


# optimal
def max_end3(nums):
    return [nums[0] if nums[0] > nums[-1] else nums[-1]] * 3


# test
if __name__ == "__main__":
    max_end3([1, 2, 3])
    max_end3([11, 5, 9])
    max_end3([2, 11, 3])
    max_end3([11, 3, 3])
    max_end3([3, 11, 11])
    max_end3([2, 2, 2])
    max_end3([2, 11, 2])
    max_end3([0, 0, 1])
