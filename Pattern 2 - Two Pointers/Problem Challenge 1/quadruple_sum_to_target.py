
# my attempt
def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    for i in range(len(arr) - 3):
        for j in range(len(arr) - 2):
            if j == i + 1 or arr[j] != arr[j - 1]:
                l, r = j + 1, len(arr) - 1
                while l < r:
                    sum = arr[i] + arr[j] + arr[l] + arr[r]
                    if sum == target:
                        quadruplets.append([arr[i], arr[j], arr[l], arr[r]])
                        l += 1
                        while (l < r and arr[l] == arr[l - 1]):
                            l += 1 
                    elif sum > target:
                        r -= 1
                    else:
                        l += 1
        
    return quadruplets


# Naive solution
def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    for i in range(len(arr) - 3):
        if i == 0 or arr[i] != arr[i - 1]:
            for j in range(i + 1, len(arr) - 2):
                if j == i + 1 or arr[j] != arr[j - 1]:
                    l, r = j + 1, len(arr) - 1
                    while l < r:
                        sum = arr[i] + arr[j] + arr[l] + arr[r]
                        if sum == target:
                            quadruplets.append([arr[i], arr[j], arr[l], arr[r]])
                            l += 1
                            while (l < r and arr[l] == arr[l - 1]):
                                l += 1  # skip same element to avoid duplicate quadruplets
                        elif sum > target:
                            r -= 1
                        else:
                            l += 1

    return quadruplets


# Generalized kSum solution
def search_quadruplets(arr, target):
    quadruplets, quadruplet = [], []

    def kSum(start, k, target):
        # base case is when k == 2, since we can reduce the problem to 2Sum w/ l & r pointers
        if k != 2:
            # while k != 2, recursively call kSum with target updated to account for the value we just processed
            for i in range(start, len(arr) - k + 1):
                if i == start or arr[i] != arr[i - 1]: 
                    quadruplet.append(arr[i])
                    kSum(i + 1, k - 1, target - arr[i])
                    quadruplet.pop()
            return

        l, r = start, len(arr) - 1
        while l < r:
            sum = arr[l] + arr[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                quadruplets.append(quadruplet + [arr[l], arr[r]])
                l += 1
                while l < r and arr[l] == arr[l - 1]:
                    l += 1

    kSum(0, 4, target)

    return quadruplets




def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()