"""
 311. Sparse Matrix Multiplication

    Total Accepted: 17228
    Total Submissions: 34262
    Difficulty: Medium
    Contributors: Admin

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [[ 1, 0, 0],[-1, 0, 3]]
B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
class Solution(object):
    def multiply0(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # Not using sparse property: TLE!
        if not A or not B: return None
        # A: l*m, B: m*n => C: l*n
        l, m, n = len(A), len(A[0]), len(B[0])
        ans = [[0 for _n in xrange(n)] for _l in xrange(l)]      # initialize by its dimension
        for i in xrange(l):
            for j in xrange(n):
                ans[i][j] = sum(A[i][k]*B[k][j] for k in xrange(m))
        return ans

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # Compress both matrix
        if not A or not B: return None
        # A: l*m, B: m*n => C: l*n
        l, m, n = len(A), len(A[0]), len(B[0])
        ans = [[0 for _n in xrange(n)] for _l in xrange(l)]      # initialize by its dimension
        AA, BB = {}, {}
        for r in xrange(l):
            for a in xrange(m):
                if A[r][a] != 0 and r not in AA:
                    AA[r] = {a: A[r][a]}
                elif A[r][a] != 0 and r in AA:
                    AA[r][a] = A[r][a]

        for c in xrange(n):
            for b in xrange(m):
                if B[b][c] != 0 and c not in BB:
                    BB[c] = {b: B[b][c]}
                elif B[b][c] != 0 and c in BB:
                    BB[c][b] = B[b][c]

        # print AA, BB

        for i, va in AA.iteritems():
            for j, vb in BB.iteritems():
                for k in va:
                    if k in vb:
                        ans[i][j] += va[k]*vb[k]
        return ans