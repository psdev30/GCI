# very first solution attempt (3/3)
# passed grokking test cases but failed on LC 
# sum = windowStart = windowEnd = 0
    # smallestLen = float('inf')
    # while windowEnd < len(arr):
    #     sum += arr[windowEnd]
    #     if sum >= s:
    #         smallestLen = min(smallestLen, windowEnd - windowStart + 1)
    #         sum = 0
    #         windowStart += 1
    #         windowEnd = windowStart
    #     else:
    #         windowEnd += 1

    # return smallestLen if smallestLen != float('inf') else 0