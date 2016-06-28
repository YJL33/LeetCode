"""
213. House Robber II

Note: This is an extension of House Robber.

After robbing those houses on that street,
the thief has found himself a new place for his thievery so that he won't get too much attention.
This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, the security system for these houses is as same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(nums):
            res = 0
            prev = 0
            if not nums:
                return res
            for i in nums:
                res, prev = max(prev+i, res), res
            return res
        if len(nums) == 1:
            return nums[0]
        else:
            return max(check(nums[1:]), check(nums[:-1]))


