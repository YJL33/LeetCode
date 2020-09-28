"""
see https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = len(nums)
        # L[i] = product of all elements BEFORE nums[i]
        # R[i] = product of all elements AFTER nums[i]
        L, R = [1 for _ in nums], [1 for _ in nums]
        for i in range(1,len(nums)):
            L[i] = L[i-1]*nums[i-1]

        for j in range(-2,-1*len(nums)-1,-1):
            R[j] = R[j+1]*nums[j+1]

        res = [0 for _ in nums]
        for i in range(len(nums)):
            res[i] = L[i]*R[i]

        # print L, R
        return res

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([9,0,-2]))