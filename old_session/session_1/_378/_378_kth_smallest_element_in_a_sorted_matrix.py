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
from heapq import heappush, heappop, heappushpop, heapify
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(matrix)
        heap = [(matrix[0][j], 0, j) for j in xrange(n)]
        heapify(heap)                               # Heapify the first row of matrix
    
        for _ in xrange(k-1):                       # Keep pop() k-1 times
            row = heap[0][1]
            col = heap[0][2]
            if row+1 < n:                           # Add new elements into heap in the meantime
                heappushpop(heap, (matrix[row+1][col], row+1, col))
            else:
                heappop(heap)                       # At the bottom of matrix

        return heap[0][0]

