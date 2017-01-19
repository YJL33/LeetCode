"""
154. Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while start < end:
            # Binary search:
            # There's a pivot inside, check whether it's in 1st half or 2nd half
            midpoint = start + (end-start)/2
            if nums[end] == nums[midpoint]:     # duplicate
                end -= 1
                if nums[end] > nums[end+1]:     # Don't miss the pivot
                    return nums[end+1]
            elif nums[end] < nums[midpoint]:    # In the 2nd half
                start = midpoint + 1
            elif nums[end] > nums[midpoint]:    # In the 1st half
                end = midpoint
            #print start, midpoint, end, nums[start], nums[midpoint], nums[end]

        return nums[start]