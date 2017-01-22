"""
46. Permutations

Given a collection of distinct numbers,
return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, len(nums), [], res)
        return res

    def helper(self, cands, countdown, path, res):
        if countdown == 0:
            res.append(path)
        for i in xrange(len(cands)):
            self.helper(cands[:i]+cands[i+1:], countdown-1, path+[cands[i]], res)
