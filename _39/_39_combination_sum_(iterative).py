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
import collections
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        stack, res = collections.deque(), []     # use a stack
        for i in xrange(len(candidates)):
            stack.append([candidates[i]])

        while stack:
            sumup = sum(stack[-1])
            if sumup == target:
                res += stack.pop(),

            elif sumup > target:
                stack.pop()

            else:
                temp = stack.pop()
                j = candidates.index(temp[-1])
                while j < len(candidates) and candidates[j]+sumup <= target:
                    stack.appendleft(temp+[candidates[j]])
                    j += 1

        return res
