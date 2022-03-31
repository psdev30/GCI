# 1st solve: 3/20
def find_permutation(str1, pattern):
  patternTracker = dict()
  windowStart = 0
  # store frequencies of all letters in given pattern
  for letter in pattern:
      patternTracker[letter] = patternTracker.get(letter, 0) + 1
  
  for windowEnd in range(len(str1)):
      letter = str1[windowEnd]
      if letter in patternTracker:
          patternTracker[letter] -= 1
          if max(patternTracker.values()) == 0:
              return True
      else:
          leftLetter = str1[windowStart]
          if leftLetter in patternTracker:
              patternTracker[leftLetter] += 1
          windowStart += 1
  
  return False
