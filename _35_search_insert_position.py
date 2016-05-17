"""
35. Search Insert Position

Given a sorted array and a target value,
return the index if the target is found.

If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Implement Binary Search
        if target > nums[-1]:
            return len(nums)        # insert at the end
        elif target == nums[-1]:
            return len(nums)-1      # insert before the end
        elif target <= nums[0]:
            return 0                # insert at the beginning
        else:
            left, m, right = 0, 0, (len(nums)-1)
            while left < right:
                m = (left+right)/2
                if nums[m] > target:        # insert between [left, m]
                    right = m-1
                    if nums[right] < target:    # m-1 < target < m
                        return m
                elif nums[m] < target:      # insert between [m+1, right]
                    left = m+1
                    if nums[left] >= target:    # m < target < m+1
                        return left
                else:                       # m = target
                    return m
            return m
