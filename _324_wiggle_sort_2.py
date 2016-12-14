"""
 324. Wiggle Sort II

    Total Accepted: 21157
    Total Submissions: 84636
    Difficulty: Medium
    Contributors: Admin

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""             
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """           
        # sort then rearrange: O(nlogn)
        # quickselect: best O(n) worst O(n^2)
        # median of median: guarantee O(n)
        # want to get something like: [4,8,3,7,2,6,1,5]
        nums.sort()
        halflen = (len(nums)/2)+1 if len(nums)%2 else len(nums)/2       # 7 => 3, 8 => 4
        nums[::2], nums[1::2] = nums[:halflen][::-1], nums[halflen:][::-1]