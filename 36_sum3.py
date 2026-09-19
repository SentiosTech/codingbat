"""
Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""


# normal
def sum3(nums):
    count = 0
    for num in nums:
        count += num
    return count


# optimal
def sum3(nums):
    return sum(nums)


# test
if __name__ == "__main__":
    sum3([1, 2, 3]) == 6
    sum3([5, 11, 2]) == 18
    sum3([7, 0, 0]) == 7
    sum3([1, 2, 1]) == 4
    sum3([1, 1, 1]) == 3
    sum3([2, 7, 2]) == 11
