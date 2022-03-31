# Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

# Example 2:
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".

# Example 3:
# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


def length_of_longest_substring(str1, k):
    letterTracker = dict()
    longestSubstr = windowStart = maxFrequency = 0
    for windowEnd in range(len(str1)):
        letter = str1[windowEnd]
        letterTracker[letter] = letterTracker.get(letter, 0) + 1
        maxFrequency = max(maxFrequency, letterTracker[letter])
        while (windowEnd - windowStart + 1) - maxFrequency > k:
            leftLetter = str1[windowStart]
            letterTracker[leftLetter] -= 1
            if letterTracker[leftLetter] == 0:
                del letterTracker[leftLetter]
            windowStart += 1
        longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)

    return longestSubstr            




def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))

main()