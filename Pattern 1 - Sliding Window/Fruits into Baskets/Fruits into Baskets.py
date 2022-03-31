# You are visiting a to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.
# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

# 1) Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# 2) You can start with any tree, but you can’t skip a tree once you have started.
# 3) You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both baskets.

# Example 1:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


# solve 1: 3/5 (looked at solution)
def fruits_into_baskets(fruits):
    maxFruits = windowStart = 0
    fruitCounts = dict()
    for windowEnd in range(len(fruits)):
        fruit = fruits[windowEnd]
        fruitCounts[fruit] = fruitCounts.get(fruit, 0) + 1
        while len(fruitCounts) > 2:
            leftFruit = fruits[windowStart]
            fruitCounts[leftFruit] -= 1
            if fruitCounts[leftFruit] == 0:
                del fruitCounts[leftFruit]
            windowStart += 1
        maxFruits = max(maxFruits, windowEnd - windowStart + 1)
    
    return maxFruits


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()