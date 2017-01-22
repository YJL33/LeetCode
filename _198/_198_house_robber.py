"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        loot = [0]*len(nums)  # loot[i] = the maximum amount of money can be robbed at house i
        loot[0] = nums[0]
        loot[1] = max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            loot[i] = max(loot[i-2]+nums[i], loot[i-1])
        return loot[-1]
