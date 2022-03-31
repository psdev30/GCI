# very first solution attempt (3/4)
# passed 3 test cases on GCI but had bugs, didn't pass on LC
# letterTracker = dict()
    # substr = ''
    # distinctCount = longestSubStr =  0
    # for windowEnd in range(len(string)):
    #     letter = string[windowEnd]
    #     if distinctCount == k and letter not in letterTracker:
    #         longestSubStr = max(longestSubStr, len(substr))
    #         substr = substr[1:]
    #     else:
    #         substr += letter
    #         if letter not in letterTracker:
    #             letterTracker[letter] = True
    #             distinctCount += 1
        
    # return longestSubStr