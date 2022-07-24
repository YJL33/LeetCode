from typing import List
class Solution(object):
    # set operation
    # maintain a set of seen sum (e.g seenSum), which contains all seen possible partial sums.
    # for each n, add itself into seenSum, and add every n+s into seenSum for all s in seenSum
    # tc: 
    # O(NlogN) to sort
    # O(N*s) for set operation, where s is the size of seenSum: propotional to target sum (sum//2)
    def canPartition_set(self, nums: List[int]) -> bool:
        if sum(nums)%2: return False
        nums = sorted(nums, reverse=True)
        target = int(sum(nums)/2)
        seenSum = set()

        for i in range(len(nums)):
            if nums[i] > target:
                return False
            if nums[i] == target or target-nums[i] in seenSum:
                return True
            elif not seenSum:
                seenSum.add(nums[i])
            else:
                toAdd = set()
                for x in seenSum:
                    newSum = x+nums[i]
                    if newSum < target and newSum not in seenSum: toAdd.add(newSum)
                seenSum = seenSum.union(toAdd)
        return False

    # DFS, top down memoization
    # tc: 
    # O(nlogn): sort
    # O(n)*O(m), where m the size of memo, worst case O(target)
    def canPartition_dfs(self, nums: List[int]) -> bool:
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False
        nums.sort(reverse=True)
        
        # try to use any j for j in range(i, n)
        def dfs(i, target):
            if target < 0: return False
            if target == 0: return True
            if target in memo: return memo[target]
            memo[target] = False
            for j in range(i, n):
                if dfs(j+1, target-nums[j]):
                    memo[target] = True
                    break
            return memo[target]
        return dfs(0, s >> 1)

    # knapsack
    # search from 0 to sum(nums)//2
    # backpack size = sum(nums)//2
    # tc: O(n*m), where m is the size of dp, propotional to sum of nums
    def canPartition_knapsack(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 != 0: return False
        target = total_sum//2

        # check the max(nums) see if we can terminate earlier
        x = max(nums)
        if x > target: return False
        if x == target: return True
        
        # dp bottom up
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for n in nums:
            for t in range(target, n-1, -1):
                dp[t] = dp[t] or dp[t-n]
            if dp[target]: return True

        return False

print(Solution().canPartition([1,5,11,5]))
print(Solution().canPartition([1,2,3,5]))
print(Solution().canPartition([3,4,2,5]))
print(Solution().canPartition([6,6,6,6,6,6,6,6]))