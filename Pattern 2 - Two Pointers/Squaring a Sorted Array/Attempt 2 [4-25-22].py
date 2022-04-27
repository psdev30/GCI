# first attempt
#time: O(2n) -> O(n)
#space: O(n) w/ output arr; O(1) otherwise
def make_squares(arr):
    squares = []
    l , r = 0, len(arr) - 1
    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            squares.append(arr[l] ** 2)
            l += 1
        else:
            squares.append(arr[r] ** 2)
            r -= 1

    # this reversal takes O(n)
    return squares[::-1]


# Ideal solution
def make_squares(arr):
    squares = [0 for i in range(len(arr))]
    l, r, idx = 0, len(arr) - 1, len(squares) - 1
    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            squares[idx] = arr[l] ** 2
            l += 1
        else:
            squares[idx] = arr[r] ** 2
            r -= 1
        idx -= 1
    
    return squares



def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()