"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        L = len(nums)
        nums.sort()

        for i in xrange(1<<L):
            tmp = []
            for j in xrange(L):
                if i & (1<<j):  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
