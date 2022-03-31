# Given a string, find the length of the longest substring, which has all distinct characters.

# Example 1:
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".

# Example 2:
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring with distinct characters is "ab".

# Example 3:
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings with distinct characters are "abc" & "cde".

def non_repeat_substring(str):
    tracker = dict()
    longestSubstr = windowStart = 0
    for windowEnd in range(len(str)):
        letter = str[windowEnd]
        tracker[letter] = tracker.get(letter, 0) + 1
        while max(tracker.values()) > 1:
            leftmostLetter = str[windowStart]
            tracker[leftmostLetter] -= 1
            if tracker[leftmostLetter] == 0:
                del tracker[leftmostLetter]
            windowStart += 1
        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)
    return longestSubstr

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()