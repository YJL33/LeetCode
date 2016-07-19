"""
152. Maximum Product Subarray

Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        local_min = nums[0]
        local_max = nums[0]
        res = nums[0]
        
        for i in xrange(1, len(nums)):
            a = nums[i]*local_min
            b = nums[i]*local_max
            c = nums[i]
            local_min = min(min(a,b), c)
            local_max = max(max(a,b), c)
            res = max(local_max, res)

        return res