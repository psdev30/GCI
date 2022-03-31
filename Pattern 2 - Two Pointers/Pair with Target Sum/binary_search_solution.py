# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example 1:
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

# Example 2:
# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11


def pair_with_target_sum(arr, target_sum):
    for i, val in enumerate(arr):
        needed = target_sum - val
        second_idx = binary_search(arr, needed)
        if second_idx != -1:
            return i, second_idx

    return [-1, -1]


def binary_search(arr, target):
    lo = 0
    hi = len(arr)
    while lo <= hi:
        mid = lo + (lo + hi) // 2
        if arr[mid] > target:
            hi -= 1
        elif arr[mid] < target:
            lo += 1
        else:
            return mid

    return -1


def main():
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))


main()