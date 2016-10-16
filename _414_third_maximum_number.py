"""
414. Third Maximum Number

    Total Accepted: 485
    Total Submissions: 1550
    Difficulty: Easy
    Contributors: Admin

Given an array of integers,
return the 3rd Maximum Number in this array,
if it doesn't exist, return the Maximum Number.
The time complexity must be O(n) or less.
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return max(nums)
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for n in nums:
            if n > first:
                first, second, third = n, first, second
            elif n < first and n > second:
                second, third = n, second
            elif n < first and n < second and n > third:
                third = n

        return third