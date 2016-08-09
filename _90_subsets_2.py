"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        nums.sort()
        res = [[]]

        for i in xrange(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:      # if not repeated
                l = len(res)                        # add new element to all existing collections
            for j in xrange(len(res)-l, len(res)):
                res.append(res[j]+[nums[i]])
        return res
