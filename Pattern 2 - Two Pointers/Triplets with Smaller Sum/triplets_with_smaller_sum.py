# two pointers
# Solution
def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        l , r = i + 1, len(arr) - 1
        while l < r:
            sum = arr[i] + arr[l] + arr[r]
            if sum < target:
                count += r - l
                l += 1
            else:
                r -= 1
    
    return count
        
            
        
            
# [-1, 1, 2, 3, 4], 5



def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()