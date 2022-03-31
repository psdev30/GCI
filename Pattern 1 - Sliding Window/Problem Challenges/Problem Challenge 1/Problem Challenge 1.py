# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# 1. abc
# 2. acb
# 3. bac
# 4. bca
# 5. cab
# 6. cba
# If a string has ‘n’ distinct characters, it will have n! permutations.

# Example 1: 
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

# Example 2: 
# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.

# Example 3: 
# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.

# Example 4:
# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

def find_permutation(str1, pattern):
    patternTracker = dict()
    matches = windowStart = 0
    # store frequencies of all letters in given pattern
    for letter in pattern:
        patternTracker[letter] = patternTracker.get(letter, 0) + 1
    
    for windowEnd in range(len(str1)):
        letter = str1[windowEnd]
        if letter in patternTracker:
            patternTracker[letter] -= 1
            if patternTracker[letter] == 0:
                matches += 1

        if matches == len(patternTracker):
            return True

        if windowEnd + 1 >= len(pattern):
            leftLetter = str1[windowStart]
            if leftLetter in patternTracker:
                if patternTracker[leftLetter] == 0:
                    matches -= 1
                patternTracker[leftLetter] += 1
            windowStart += 1
    
    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()

