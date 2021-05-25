"""
40. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.helper(candidates, target, result)
        return result

    def helper(self, cands, target, res, path=[]):
        for i in xrange(len(cands)):
            if cands[i] == target:
                res.append(path+[cands[i]])
                return
            elif cands[i] > target:
                break
            if i>0 and cands[i] == cands[i-1]:          # avoid duplicate after cands[0]
                continue
            self.helper(cands[i+1:], target-cands[i], res, path+[cands[i]])
        return