"""
see https://leetcode.com/problems/maximum-subarray/
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # naive approach:
        # evaluate all subarray
        # list all subarray: O(n^2)
        # sum of all subarray: O(n^3)

        # optimization:
        # DP?
        # still around O(n^2)

        # greedy?
        if not nums:
            return 0

        local, res = nums[0], nums[0]

        for i in range(1, len(nums)):
            local = max(nums[i], local+nums[i])
            res = max(local, res)

        return res

print Solution().maxSubArray([1,2,3])
print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
