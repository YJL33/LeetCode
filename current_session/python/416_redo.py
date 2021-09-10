# eliminate edge cases first

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False
        nums.sort(reverse=True)
        
        def dfs(i, target):
            if target not in memo:
                memo[target] = False
                if target > 0:
                    for j in range(i, n):
                        if dfs(j+1, target-nums[j]):
                            memo[target] = True
                            break
            return memo[target]

        return dfs(0, s >> 1)

    def canPartition2(self, nums: List[int]) -> bool:
        sumOfNums = sum(nums)
        if sumOfNums&1: return False
        nums.sort()
        target = sumOfNums//2
        if nums[-1] > target: return False
        
        seenSum = set()
        # use seenSum (set)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target or target-nums[i] in seenSum: return True
            if not seenSum:
                seenSum.add(nums[i])
            else:
                toAdd = set()
                for x in seenSum:
                    newSum = x+nums[i]
                    if newSum not in seenSum and newSum < target: toAdd.add(newSum)
                seenSum = seenSum.union(toAdd)
        return False

print(Solution().canPartition([1,5,11,5]))
print(Solution().canPartition([1,2,3,5]))
print(Solution().canPartition([3,4,2,5]))
print(Solution().canPartition([6,6,6,6,6,6,6,6]))