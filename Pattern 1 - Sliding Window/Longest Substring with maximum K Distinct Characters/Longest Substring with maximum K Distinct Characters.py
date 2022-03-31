# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Example 3:
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

# Example 4:
# Input: String="cbbebi", K=10
# Output: 6
# Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".


# solve 1: 3/4 (looked at solution)
def longest_substring_with_k_distinct(string, k):
    letterTracker = dict()
    windowStart = maxSubStr = 0
    for windowEnd in range(len(string)):
        letter = string[windowEnd]
        if letter not in letterTracker:
            letterTracker[letter] = 0
        letterTracker[letter] += 1

        while len(letterTracker) > k:
            leftmostLetter = string[windowStart]
            letterTracker[leftmostLetter] -= 1
            if letterTracker[leftmostLetter] == 0:
                del letterTracker[leftmostLetter]
            windowStart += 1
        maxSubStr = max(maxSubStr, windowEnd - windowStart + 1)
    return maxSubStr
    
    



def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()