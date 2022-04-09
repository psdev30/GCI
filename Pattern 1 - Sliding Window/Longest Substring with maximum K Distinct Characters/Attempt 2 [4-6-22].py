# Given a string, find the length of the longest substring in it with no more than K distinct characters.

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

# solve 2: 4/6/22 (one bug --> if instead of while)
#time: O(2n) -> O(n)
#space: O(K + 1)
# https://www.notion.so/Longest-Substring-with-maximum-K-Distinct-Characters-38076943c5234420a230a239c6d89d64
def longest_substring_with_k_distinct(string, k):
    letterTracker = dict()
    longestSubstr = windowStart = 0
    for windowEnd in range(len(string)):
        letter = string[windowEnd]
        letterTracker[letter] = letterTracker.get(letter, 0) + 1
        while len(letterTracker) > k:
            leftLetter = string[windowStart]
            letterTracker[leftLetter] -= 1
            if letterTracker[leftLetter] == 0:
                del letterTracker[leftLetter]
            windowStart += 1

        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)

    return longestSubstr
     


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 10)))


main()