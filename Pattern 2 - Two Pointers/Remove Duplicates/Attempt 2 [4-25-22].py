def remove_duplicates(arr):
    l = 0
    for r in range(1, len(arr)):
        if arr[l] != arr[r]:
            l += 1

    return l

# Solution
#time: O(n)
#space: O(1)
# def remove_duplicates(arr):
#     l = 0
#     for r in range(1, len(arr)):
#         if arr[l] != arr[r]:
#             l += 1
#             arr[l] = arr[r]


#     return l + 1


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()