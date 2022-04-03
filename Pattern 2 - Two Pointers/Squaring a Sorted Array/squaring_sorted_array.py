# Problem Statement
# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Example 1:
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

# Example 2:
# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]

# Attempt 1: 4/3/22
# had right idea of left + right pointers from start to end; couldn't figure out how to handle negative case with 0 in middle of array
# https://www.notion.so/Squaring-a-Sorted-Ar-6e0bcf489fc243b09cb91e07f4e1d8de
def make_squares(arr):
    squares = []
    left, right = 0, len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            squares.append(arr[left] * arr[left])
            left += 1
        else:
            squares.append(arr[right] * arr[right])
            right -= 1  
    
    return squares[::-1]



    #time: O(n)
    #space: O(1) (not including output array)
    #clock: 5 min
    squares = []
    left, right = 0, len(arr) - 1
    while left <= right:
        if abs(arr[left]) < abs(arr[right]):
            squares.append(arr[left] * arr[left])
            left += 1
        else:
            squares.append(arr[right] * arr[right])
            right -= 1

    return squares


    #time: O(n + nlogn)
    #space: O(1) (not counting output array)
    # clock: 4 min
    squares = []
    for num in arr:
        squares.append(num * num)
    return squares.sort()



def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()