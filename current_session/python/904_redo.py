from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # use DP
        # dp = [type1, type2, beginning of current streak, begining of next streak]

        # initialize
        type1, start1 = fruits[0], 0
        i = 1
        while i < len(fruits) and fruits[i] == type1: i += 1
        if i == len(fruits): return len(fruits)
        type2, start2 = fruits[i], i
        
        fruits.append(-1)       # add a non-exist fruit at the end for easier calculation
        maxSeen = i+1
        for j in range(i+1, len(fruits)):
            fruitType = fruits[j]
            # see if this fruit type belong to current streak or not
            # if fruitType in [type1, type2]
            # update the start if necessary 

            if fruitType == type2:
                continue
            elif fruitType == type1:
                type1, type2, start2 = type2, type1, j
            # we should start from 2nd type of fruit and see if there's a longer streak
            else:
                maxSeen = max(maxSeen, j-start1)
                type1, type2, start1, start2 = type2, fruits[j], start2, j
        fruits.pop()            # restore the array (if necessary)

        return maxSeen

# print(Solution().totalFruit())
print(Solution().totalFruit([1,2,1]))
print(Solution().totalFruit([0,1,2,2]))
print(Solution().totalFruit([1,2,3,2,2]))
print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
print(Solution().totalFruit([3,3,3,1,2,1,1,1,3,3,3]))