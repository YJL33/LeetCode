"""
45. Jump Game II

    Total Accepted: 74083
    Total Submissions: 286822
    Difficulty: Hard

Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # implement dp
        # dp[i] = minimum number of jumps to reach index i
        # dp[0] = 0, float('inf') = unchecked

        dp = [float('inf')]*len(nums)
        reach, pos, dp[0] = 0, 0, 0
        while reach != len(nums):
            step = nums[pos]
            while pos+step >= reach and reach < len(nums):
                #print pos, step, reach
                dp[reach] = min(dp[reach], dp[pos]+1)
                reach += 1
            pos += 1

        return dp[-1]
