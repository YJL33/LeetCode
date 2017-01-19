"""
47. Permutations II

Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.helper(nums, len(nums), res)
        return res

    def helper(self, cands, countdown, res, path=[]):
        if countdown == 0:
            res.append(path)
        for i in xrange(len(cands)):
            if i>0 and cands[i] == cands[i-1]:
                continue
            self.helper(cands[:i]+cands[i+1:], countdown-1, res, path+[cands[i]])
