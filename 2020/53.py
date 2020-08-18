"""
https://leetcode.com/problems/maximum-subarray/
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy
        if not nums: return 0
        
        tmp = maxSeen = nums[0]

        for n in nums[1:]:
            tmp = max(n, tmp+n)             # optimal local sum
            maxSeen = max(maxSeen, tmp)     # optimal global sum

        return maxSeen

print Solution().maxSubArray([1,2,3])