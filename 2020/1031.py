"""
see https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
"""
class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        # naive approach
        # if L < M
        # find (and sort based on sum) all sub-array length == L
        # find (and sort based on sum) all sub-array length == M
        # use dp to store partial-sum of sub-arrays
        # O(n^2)
        
        ls = [(sum(A[:L]), 0)]      # ls[i] = (a, b) = partial sum (a) from index b with length L
        ms = [(sum(A[:M]), 0)]

        for i in range(1,len(A)-L+1):
            p = ls[-1][0] - A[i-1] + A[i-1+L]
            ls += (p, i),

        for i in range(1,len(A)-M+1):
            p = ms[-1][0] - A[i-1] + A[i-1+M]
            ms += (p, i),

        res = 0
        for i in range(len(ls)):
            for j in range(len(ms)):
                if not (i <= j and j <= i+L-1) and not (j <= i and i <= j+M-1):
                    res = max(res, ls[i][0] + ms[j][0])

        return res

print(Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))
print(Solution().maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2))
print(Solution().maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3))