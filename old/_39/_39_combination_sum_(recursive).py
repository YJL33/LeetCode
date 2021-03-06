"""
39. Combination Sum

Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.helper(candidates, target, [], res)
        return res

    def helper(self, cands, target, path, res):
        if target == 0:
            res.append(path)
        for i in xrange(len(cands)):
            if target < cands[i]:
                break
            self.helper(cands[i:], target-cands[i], path+[cands[i]], res)
        return