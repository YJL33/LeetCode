"""
198
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0

        # use dp
        # keep update two variables: max amount with i and without i
        dp_without = 0
        dp_with = nums[0]
        maxSeen = nums[0]

        for i in range(1,len(nums)):
            dp_with, dp_without = nums[i]+dp_without, max(dp_with, dp_without)

        return max(dp_with, dp_without)