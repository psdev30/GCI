# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray 
# whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Example 1:
# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

# Example 2:
# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# Example 3:
# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
# or [1, 1, 6].

def smallest_subarray_sum(s, arr):
    smallestLen = float('inf')
    windowStart = sum = 0
    for windowEnd in range(len(arr)):
        sum += arr[windowEnd]
        while sum >= s:
            smallestLen = min(smallestLen, windowEnd - windowStart + 1)
            sum -= arr[windowStart]
            windowStart += 1
    
    return smallestLen if smallestLen != float('inf') else 0


def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))

main()