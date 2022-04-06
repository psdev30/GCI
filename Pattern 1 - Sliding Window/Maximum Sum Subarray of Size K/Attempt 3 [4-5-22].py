# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:
# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# Attempt 3: 4/5/22
#time: O(n)
#space: O(1)
# https://www.notion.so/Maximum-Sum-Subarray-of-Size-K-6e76c44491b5472789cd528d94595c23
def max_sub_array_of_size_k(k, arr):
    windowStart = sum = maxSum = 0
    for windowEnd in range(len(arr)):
        sum += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, sum)
            sum -= arr[windowStart]
            windowStart += 1
    
    return maxSum
    

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(k=3, arr=[2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(k=2, arr=[2, 3, 4, 1, 5])))


main()