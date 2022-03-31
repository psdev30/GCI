# first attempt (WRONG)
def find_substring(str1, pattern):
    patternTracker = dict()
    for letter in pattern:
        patternTracker[letter] = patternTracker.get(letter, 0) + 1

    matches = windowEnd = windowStart = 0
    smallest = float('inf')
    leftIdx = rightIdx = -1
    while windowStart < len(str1) and windowEnd < len(str1):
        letter = str1[windowEnd]
        if letter in patternTracker:
            patternTracker[letter] -= 1
            if patternTracker[letter] == 0:
                matches += 1
        
        if matches == len(pattern):
            if windowEnd - windowStart + 1 < smallest:
                leftIdx = windowStart
                rightIdx = windowEnd
                smallest = windowEnd - windowStart + 1
            leftLetter = str1[windowStart]
            if leftLetter in patternTracker:
                if patternTracker[leftLetter] < 0:
                    matches -= 1
                patternTracker[leftLetter] += 1
            windowStart += 1

        if windowEnd < len(str1) - 1:
            windowEnd += 1

    return str1[leftIdx : rightIdx + 1]