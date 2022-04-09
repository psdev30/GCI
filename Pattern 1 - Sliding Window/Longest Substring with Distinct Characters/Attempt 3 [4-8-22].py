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

# attempt 3: got close to optimal but not quite
#time: O(2n) -> O(n)
#space: O(n)
# https://www.notion.so/Longest-Substring-with-Distinct-Characters-ea79bc31ba1243009fa065df08d7c0b0
def non_repeat_substring(str):
    # ideal solution
    letterTracker = set()
    longest = windowStart = 0
    for windowEnd in range(len(str)):
        letter = str[windowEnd]
        while letter in letterTracker:
            letterTracker.remove(str[windowStart])
            windowStart += 1
        letterTracker.add(letter)

        longest = max(longest, windowEnd - windowStart + 1)
    
    return longest
# -------------------------------------------------------------------------------------------
    # my attempt
    letterTracker = dict()
    longest = windowStart = 0
    for windowEnd in range(len(str)):
        letter = str[windowEnd]
        letterTracker[letter] = letterTracker.get(letter, 0) + 1

        while max(letterTracker.values()) > 1:
            leftLetter = str[windowStart]
            letterTracker[leftLetter] -= 1
            windowStart += 1

        longest = max(longest, windowEnd - windowStart + 1)

    return longest


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()