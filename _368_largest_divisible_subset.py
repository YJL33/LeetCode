"""
368. Largest Divisible Subset

Given a set of distinct positive integers,
find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)

Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import math
        from copy import copy
        nums.sort()             # now the list is ascending. if nums[i] % nums[j] == 0, i must >= j
        length = len(nums)      # e.g. 9 % 3 == 0, 3 % 9 == 3
        if not nums:
            return []
        # list dp[i] => record nums[i]'s every divider (factor)
        dp = [[nums[x]] for x in xrange(length)]      # each number must have itself as divider
        # for any nums[i], find the maximum j s.t. nums[i] % nums[j]==0
        # then dp[i] = [nums[i]] + dp[j]
        max_len = 0
        max_index = 0
        for i in xrange(1, length):
            maxSet = []
            for j in xrange(i-1, -1, -1):
                if nums[j] <= nums[i]/2:
                    if nums[i] % nums[j] == 0:
                        localSet = copy(dp[j])
                        if len(localSet) > len(maxSet):
                            maxSet = localSet

            maxSet.append(nums[i])
            dp[i] = maxSet
            
            if len(dp[i]) > max_len:
                max_len = len(dp[i])
                max_index = i
        
        return dp[max_index]