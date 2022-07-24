import heapq
from typing import List
class Solution:
    def minimumDifference(self, A: List[int]) -> int:
        # pick some to the left, some to the right
        # make left as small as possible, right as big as possible
        N = len(A)
        k = N//3
        s = sum(A)
        
        # like draft
        # use a max_heap at left side, and we keep the size of heap
        # (by pop out the bigger elements)
        # left array is the optimal choice from 0 to k / 2k-1
        left = [sum([a for a in A[:k]])]
        max_heap = [-1*a for a in A[:k]]
        heapq.heapify(max_heap)                     # O(klogk)
        
        for i in range(k, 2*k):                     # O(klogk)
            heapq.heappush(max_heap, -1*A[i])
            x = -1*heapq.heappop(max_heap)
            left.append(left[-1]+A[i]-x)
        
        # do the same for right side array
        right = [sum([a for a in A[2*k:]])]
        min_heap = [a for a in A[2*k:]]
        heapq.heapify(min_heap)

        for j in range(2*k-1, k-1, -1):
            heapq.heappush(min_heap, A[j])
            x = heapq.heappop(min_heap)
            right.append(right[-1]+A[j]-x)
        
        right.reverse()
        assert(len(left) == len(right))
        # print(left)
        # print(right)
        
        return min([left[i]-right[i] for i in range(len(left))])