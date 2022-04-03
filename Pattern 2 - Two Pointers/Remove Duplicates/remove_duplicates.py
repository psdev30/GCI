# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

# Example 1:
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

# Example 2:
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

# Attempt 1: 4/3/22
# had basic idea of two pointers, one fast & one slow, but couldn't get working solution
def remove_duplicates(arr):
    slow = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[slow]:
            arr[slow] = arr[i]
            slow += 1
    
    return slow


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()