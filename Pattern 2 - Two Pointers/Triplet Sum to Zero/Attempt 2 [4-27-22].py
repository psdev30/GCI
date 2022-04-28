# first attempt
def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 or arr[i] != arr[i - 1]:
            l, r = i + 1, len(arr) - 1
            while l < r:
                sum = arr[i] + arr[l] + arr[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    triplets.append([arr[i], arr[l], arr[r]])
                    l += 1
                    while arr[l] == arr[l - 1]:
                        l += 1
    
    return triplets


# second attempt
#time: O(nlogn + n^2)
#space: O(n) -> timsort space + output array
def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            l, r = i + 1, len(arr) - 1
            while l < r:
                sum = arr[i] + arr[l] + arr[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    triplets.append([arr[i], arr[l], arr[r]])
                    l += 1
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1
    
    return triplets
        
# [-2, -2, 0, 0, 2, 2]

# [-3, -2, -1, 0, 1, 1, 2]
# [-5, -2, -1, 2, 3]



def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()