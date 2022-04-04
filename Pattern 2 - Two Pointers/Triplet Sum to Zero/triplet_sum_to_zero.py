# Problem Statement
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.

# Example 2:
# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

# Attempt 1: 4/3/22
# NS
# got the idea of using a regular pointer that iterates thru array and reducing problem to two sum within that pointer
# https://www.notion.so/Triplet-Sum-to-Zero-1d74b99e1e50407480c726bd66684dcd
def search_triplets(arr):
    triplets = []
    arr.sort()
    for i in range(len(arr) - 2):
        # if i > 0 and arr[i] == arr[i - 1]:
        #     continue
        needed = -1 * arr[i]
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[left] + arr[right]
            if sum > needed:
                right -= 1
            elif sum < needed:
                left += 1
            else:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                while arr[left] == arr[left - 1] and left < right:
                    left += 1

    return triplets




def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()

