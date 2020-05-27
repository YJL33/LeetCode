"""
52. N-Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations,
return the total number of distinct solutions.
"""
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(queens=[], xy_dif=[], xy_sum=[]):
            p = len(queens)
            if p==n:
                result.append(queens)
                return
            for q in xrange(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        dfs()
        return len(result)