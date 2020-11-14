"""
https://leetcode.com/problems/maximum-product-subarray/
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # naive approach: check the product of all nums[i:j]
        # O(n^3)

        # move from left to right
        # at each point, check the previous value
        # (local max and global max)
        # O(n) (?)

        if not nums: return None

        localMax, localMin, globalMax = nums[0], nums[0], nums[0]

        for n in nums[1:]:
            localMin, localMax = min(n, localMin*n, localMax*n), max(n, localMax*n, localMin*n)
            globalMax = max(localMax, globalMax)

        return globalMax

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,1]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([10]))
print(Solution().maxProduct([]))