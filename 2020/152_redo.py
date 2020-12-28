"""
https://leetcode.com/problems/maximum-product-subarray/
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # beware of negative
        # dp: for each i, we store the max + and - with i as end point
        # improvement:
        # we don't need to store for each index
        # simply keep update the previous one
        if not nums: return None
        dp = (nums[0],nums[0])
        maxSeen = nums[0]
        for i in range(1,len(nums)):
            n1 = max(nums[i]*dp[0], nums[i]*dp[1], nums[i])
            n2 = min(nums[i]*dp[0], nums[i]*dp[1], nums[i])
            dp = (n1, n2)
            maxSeen = max(maxSeen, n1, n2)

        return maxSeen

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,1]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([10]))
print(Solution().maxProduct([]))
