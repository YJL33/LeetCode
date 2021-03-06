"""
34. Search for a Range

Given a sorted array of integers,
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def getstart(low, high):
            while low < high:
                mid = (low + high) / 2
                if nums[mid] < target:
                    low = mid+1
                else:
                    high = mid
            return low

        def getend(left, right):
            while left < right:
                m = ((left + right) / 2) +1
                if nums[m] <= target:
                    left = m
                else:
                    right = m-1
            return right

        if target < nums[0] or target > nums[-1]: return [-1, -1]
        start = getstart(0, len(nums)-1)
        if nums[start] != target: return [-1, -1]
        end = getend(start, len(nums)-1)
        if nums[end] == target: return [start, end]
