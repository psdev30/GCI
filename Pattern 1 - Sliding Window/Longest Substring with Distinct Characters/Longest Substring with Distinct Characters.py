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


# solve 1: 3/7 (got it! :))
def non_repeat_substring(str):
    letterTracker = set()
    longestSubstring = windowStart = 0
    for windowEnd in range(len(str)):
        letter = str[windowEnd]
        while letter in letterTracker:
            letterTracker.remove(str[windowStart])
            windowStart += 1
        letterTracker.add(letter)
        longestSubstring = max(longestSubstring, len(letterTracker))

    return longestSubstring


    letterTracker = dict()
    longestSubstring = windowStart = 0
    for windowEnd in range(len(str)):
        letter = str[windowEnd]
        letterTracker[letter] = letterTracker.get(letter, 0) + 1
        while max(letterTracker.values()) > 1:
            leftLetter = str[windowStart]
            letterTracker[leftLetter] -= 1
            if letterTracker[leftLetter] == 0:
                del letterTracker[leftLetter]
            windowStart += 1
        longestSubstring = max(longestSubstring, windowEnd - windowStart + 1)

    return longestSubstring

    letterTracker = set()
    maxSubstring = windowStart = 0
    for windowEnd in range(len(str)):
        letter = str[windowEnd]
        if letter not in letterTracker:
            letterTracker.add(letter)
            maxSubstring = max(maxSubstring, windowEnd - windowStart + 1)
        else:
            letterTracker.remo
            windowStart += 1
        maxSubstring = max(maxSubstring, windowEnd - windowStart + 1)

    return maxSubstring

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()