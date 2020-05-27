"""
88. Merge Sorted Array

Given two sorted integer arrays M and N, merge N into M as one sorted array.

Note:
You may assume that M has enough space
(size that is greater or equal to m + n) to hold additional elements from N.
The number of elements initialized in M and N are m and n respectively.
"""
class Solution(object):
    def merge(self, M, m, N, n):
        """
        :type M: List[int]
        :type m: int
        :type N: List[int]
        :type n: int
        :rtype: void Do not return anything, modify M in-place instead.
        """
        pos = m+n-1         # beginning from the end, check with index m-1 and n-1
        while n > 0:                                # end loop when n == 0
            if m <= 0 or N[n-1] >= M[m-1]:
                M[pos] = N[n-1]
                n -= 1                              # N move 1 step forward
            else:
                M[pos] = M[m-1]
                m -= 1                              # M move 1 step forward
            pos -= 1
        return