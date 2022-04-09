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
    # my attempt
    # passes GCI test cases but fails LC 
    tracker = dict()
    longest = windowStart = 0
    for windowEnd in range(len(str1)):
        letter = str1[windowEnd]
        tracker[letter] = tracker.get(letter, 0) + 1
        while sum(tracker.values()) - tracker[str1[windowStart]] > k:
            leftLetter = str1[windowStart]
            tracker[leftLetter] -= 1
            windowStart += 1
        
        longest = max(longest, windowEnd - windowStart + 1)

    return longest

    # attempt after looking at O(26n) conceptual explanation 
    tracker = dict()
    longest = windowStart = 0
    for windowEnd in range(len(str1)):
        letter = str1[windowEnd]
        tracker[letter] = tracker.get(letter, 0) + 1
        while (windowEnd - windowStart + 1) - max(tracker.values()) > k:
            leftLetter = str1[windowStart]
            tracker[leftLetter] -= 1
            windowStart += 1
        
        longest = max(longest, windowEnd - windowStart + 1)
    
    return longest

    # looked at complete O(n) solution
    tracker = dict()
    longest = maxRepeatingChar = windowStart = 0
    for windowEnd in range(len(s)):
        letter = s[windowEnd]
        tracker[letter] = tracker.get(letter, 0) + 1
        maxRepeatingChar = max(maxRepeatingChar, tracker[letter])
        while (windowEnd - windowStart + 1) - maxRepeatingChar > k:
            leftLetter = s[windowStart]
            tracker[leftLetter] -= 1
            windowStart += 1

        longest = max(longest, windowEnd - windowStart + 1)

    return longest


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()