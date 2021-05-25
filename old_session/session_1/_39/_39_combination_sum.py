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
        candidates.sort()
        combinations = [[c] for c in candidates]    # possible combinations
        res = []                                    # final result
        count = len(combinations)                   # count of un-checked possible combinations
        i = 0                                       # index of possible combinations
        while count > 0:    
            s = sum(combinations[i])                # check each possible combination
            if s == target:                         # if equal to target...
                res.append(combinations[i])         # ... append it into result
            elif s < target:                        # if less than target...
                #print "not enough"
                j = candidates.index(combinations[i][-1]) # ..check the last element in combination
                while j < len(candidates) and s+candidates[j] <= target:    # ... if s+c[j] valid
                    #print candidates[j]
                    combinations.append(combinations[i]+[candidates[j]])    # ... add it
                    count += 1                          # ... add one more un-checked combination
                    #print combinations
                    j += 1
            i += 1                                  # next un-checked combination
            count -= 1                              # minus one un-checked combination

        return res
