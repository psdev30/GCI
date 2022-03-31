# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1: 
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

# Example 2: 
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

def length_of_longest_substring(arr, k):
    longestSubstr = windowStart = maxOnesCnt = 0
    for windowEnd in range(len(arr)):
        num = arr[windowEnd]
        if num == 1:
            maxOnesCnt += 1
        while (windowEnd - windowStart + 1) - maxOnesCnt > k:
            if arr[windowStart] == 1:
                maxOnesCnt -= 1
            windowStart += 1
        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)
    return longestSubstr

def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()