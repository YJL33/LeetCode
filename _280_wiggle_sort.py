"""
280. Wiggle Sort

    Total Accepted: 15422
    Total Submissions: 29508
    Difficulty: Medium

Given an unsorted array nums,
reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag, stack = True, []		# flag = True: looking for bigger number, vice versa
        for i in xrange(len(nums)):
        	if i+1 == len(nums):
        		break
        	if flag and nums[i+1] < nums[i]:
        		nums[i], nums[i+1] = nums[i+1], nums[i]
        	elif not flag and nums[i+1] > nums[i]:
        		nums[i], nums[i+1] = nums[i+1], nums[i]
        	flag = not flag
