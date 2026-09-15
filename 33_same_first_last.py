"""Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True"""


# optim
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


if __name__ == "__main__":
    print(same_first_last([1, 2, 3]))  # False
    print(same_first_last([1, 2, 3, 1]))  # True
    print(same_first_last([1, 2, 1]))  # True
    print(same_first_last([]))  # False
    print(same_first_last([7]))  # True
