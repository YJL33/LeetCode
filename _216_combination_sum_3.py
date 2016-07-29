"""
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used,
and each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]


Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        import itertools
        res = []
        upper_lim = min(9, (n - sum(range(1,10)[:k-1])))
        lower_lim = max(1, (n - sum(range(9,0,-1)[:k-1])))
        #print lower_lim, upper_lim
        for c in itertools.combinations(range(lower_lim,upper_lim+1), k):
            if sum(c) == n:
                res.append(list(c))
        
        return res