"""
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length. 
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using no "del", costs less time => O(n)
        res = 0
        for cur in xrange(len(nums)):
            if res < 2 or nums[cur] > nums[res-2]:
                nums[res] = nums[cur]
                res += 1

        return res