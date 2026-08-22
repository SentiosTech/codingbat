"""
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""


# normal
def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


# optimal
def array_count9(nums):
    return len([num for num in nums if num == 9])


# test
if __name__ == "__main__":
    array_count9([1, 2, 9]) == 1
    array_count9([1, 9, 9]) == 2
    array_count9([1, 9, 9, 3, 9]) == 3
    array_count9([1, 2, 3]) == 0
    array_count9([]) == 0
    array_count9([4, 2, 4, 3, 1]) == 0
    array_count9([9, 2, 4, 3, 1]) == 1
