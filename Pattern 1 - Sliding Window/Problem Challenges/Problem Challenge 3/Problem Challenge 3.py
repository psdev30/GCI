# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

# Example 1:
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

# Example 2:
# Input: String="aabdec", Pattern="abac"
# Output: "aabdec"
# Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"

# Example 3:
# Input: String="abdbca", Pattern="abc"
# Output: "bca"
# Explanation: The smallest substring having all characters of the pattern is "bca".

# Example 4:
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

def find_substring(str1, pattern):
    patternTracker = dict()
    window_start = matches = startIdx = 0
    shortestSubstr = float('inf')

    for letter in pattern:
        patternTracker[letter] = patternTracker.get(letter, 0) + 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        letter = str1[window_end]
        if letter in patternTracker:
            patternTracker[letter] -= 1
            if patternTracker[letter] >= 0:  # Count every matching of a character
                matches += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matches == len(pattern):
            if shortestSubstr > window_end - window_start + 1:
                shortestSubstr = window_end - window_start + 1
                startIdx = window_start

            leftLetter = str1[window_start]
            window_start += 1
            if leftLetter in patternTracker:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if patternTracker[leftLetter] == 0:
                    matches -= 1
                patternTracker[leftLetter] += 1

    return "" if shortestSubstr > len(str1) else str1[startIdx : startIdx + shortestSubstr]
    

def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    # print(find_substring("abdbca", "abc"))
    # print(find_substring("adcad", "abc"))


main()