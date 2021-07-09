"""
https://leetcode.com/problems/find-the-duplicate-number/
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # len(nums) = n+1
        # create an array which is a counter for arr[i] is count for i
        arr = [0 for _ in range(len(nums))]
        for n in nums:
            arr[n] += 1
            if arr[n] > 1:
                return n