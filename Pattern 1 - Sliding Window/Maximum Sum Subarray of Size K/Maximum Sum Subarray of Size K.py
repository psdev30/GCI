# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:
# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].


# time: O(n)
# space: O(1)
def max_sub_array_of_size_k(k, arr):
    # solve 1: looked at solution (3/2)
    max_sum = sum = window_start = 0
    for window_end in range(len(arr)):
        sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, sum)
            sum -= arr[window_start]
            window_start += 1

    return max_sum


    # solve 2: (3/3)
    # some help (for sum -= arr[windowStart])
    # if (windowEnd - windowStart + 1) == k: shows lack of understanding.. windowEnd jumps out until there is the sufficient
    # gap btwn it and windowStart (k - 1) (or until array is of length k)
    # once we know that, each subsequent iteration of for loop will require us to check for a possible maxSum bc the array
    # is already at the max length of k
    windowStart = sum = maxSum = 0
    for windowEnd in range(len(arr)):
        sum += arr[windowEnd]
        if (windowEnd - windowStart + 1) == k:
            maxSum = max(maxSum, sum)
            sum -= arr[windowStart]
            windowStart += 1 

    return maxSum




def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(k=3, arr=[2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(k=2, arr=[2, 3, 4, 1, 5])))

main()