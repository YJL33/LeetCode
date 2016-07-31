"""
153. Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while nums[start] > nums[end]:
            # Binary search:
            # There's a pivot inside, check whether it's in 1st half or 2nd half
            midpoint = start + (end-start)/2
            if nums[start] > nums[midpoint]:        # In the 1st half
                end = midpoint
            else:                                   # In the 2nd half
                start = midpoint + 1

        return nums[start]
