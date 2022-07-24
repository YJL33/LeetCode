from typing import List
import bisect
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # use binary search
        # use heap
        # make a guess, and check each row and count how many items are smaller or equal to guess
        # say count == x
        # if x > k: guess is too big -> guess smaller -> r = m
        # if x == k: nice guess, but keep guess and make it as small as possible
        # if x < k: guess is too small
        # time O(nlogn * log(S)), where S=span of min to max
        # space O(1)

        l, r = matrix[0][0], matrix[-1][-1]

        # within the matrix, count how many items are smaller or equal to x
        def count(x):
            cnt = 0
            for r in matrix:
                cnt += bisect.bisect_right(r, x)
            return cnt

        while l < r:
            m = (l+r)//2
            if count(m) >= k:
                r = m
            else:
                l = m+1
        return r


    def kthSmallest_heap(self, matrix: List[List[int]], k: int) -> int:
        # heap:
        # prepare a minheap that has size == row, and put all row[0] into the heap
        # do the following k times: pop the smallest one from the minHeap, and refill one from its row (until there's no more)
        # time O(k*log(N^2))
        # space O(N)
        
        ans = None
        n = len(matrix)
        hp = [(matrix[i][0],i,0) for i in range(n)]
        heapq.heapify(hp)
        
        while k:
            ans, row, col = heapq.heappop(hp)
            if col+1 < n:
                heapq.heappush(hp, (matrix[row][col+1], row, col+1))
            k -= 1
        
        return ans