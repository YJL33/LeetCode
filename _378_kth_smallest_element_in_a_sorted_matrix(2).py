"""
378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≦ k ≦ n2.
"""
import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            mid = (low+high) >> 1
            num = 0                 # count how many numbers lower than mid
            for row in matrix:
                num += bisect.bisect(row, mid)
            if num < k:             # should be at higher part
                low = mid + 1
            else:                   # should be at lower part
                high = mid

        return low
