# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!
# N!
#  permutations (or anagrams) of a string having N
# N
#  characters. For example, here are the six anagrams of the string “abc”:

# 1. abc
# 2. acb
# 3. bac
# 4. bca
# 5. cab
# 6. cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

# Example 2:
# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


def find_string_anagrams(str1, pattern):
    patternTracker = dict()
    for letter in pattern:
        patternTracker[letter] = patternTracker.get(letter, 0) + 1

    result_indexes = []
    matches = windowStart = 0
    for windowEnd in range(len(str1)):
        letter = str1[windowEnd]
        if letter in patternTracker:
            patternTracker[letter] -= 1
            if patternTracker[letter] == 0:
                matches += 1

        if matches == len(patternTracker):
            result_indexes.append(windowStart)

        if windowEnd >= len(pattern) - 1:
            leftLetter = str1[windowStart]
            if leftLetter in patternTracker:
                if patternTracker[leftLetter] == 0:
                    matches -= 1
                patternTracker[leftLetter] += 1
            windowStart += 1

    return result_indexes
    

def main():
    # print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()