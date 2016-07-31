"""
238. Product of Array Except Self

Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product of all the elements of nums,
but except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?

Note:
The output array does not count as extra space for the purpose of space complexity analysis.
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lens = len(nums)

        output = [1]*lens
        right = 1
        left = 1

        # multiply twice, from left to right
        for i in xrange(lens):
            output[i] = left
            left *= nums[i]
        # and right to left
        for j in xrange(lens-1, -1, -1):
            output[j] *= right
            right *= nums[j]

        return output
