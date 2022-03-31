def find_string_anagrams(str1, pattern):
    patternTracker = dict()
    for letter in pattern:
        patternTracker[letter] = patternTracker.get(letter, 0) + 1

    result_indexes = []
    startIdx = matches = windowStart = 0
    for windowEnd in range(len(str1)):
        letter = str1[windowEnd]
        if letter in patternTracker and patternTracker[letter] != 0:
            patternTracker[letter] -= 1
            if patternTracker[letter] == 0:
                matches += 1
        else:
            leftLetter = str1[windowStart]
            if leftLetter in patternTracker:
                patternTracker[leftLetter] += 1
                startIdx += 1
                matches -= 1
                windowStart += 1
            if letter in patternTracker:
                patternTracker[letter] -= 1
            if patternTracker[letter] == 0:
                matches += 1

        if matches == len(patternTracker):
            result_indexes.append(startIdx)

        if windowEnd - windowStart + 1 >= len(pattern):
            leftLetter = str1[windowStart]
            if leftLetter in patternTracker:
                patternTracker[leftLetter] += 1
                startIdx += 1
                matches -= 1
                windowStart += 1
        

    return result_indexes