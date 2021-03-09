"""
239
"""
from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        res = []
        maxHeap = [-1*x for x in A[:k]]
        toPop = []
        heapq.heapify(maxHeap)
        for i in range(len(A)-k):      # starting from i
            res.append(-1*maxHeap[0])
            # print('mxh @ i:', maxHeap, 'window=', A[i:i+k])

            # prepare for i+1
            # pop the maxHeap only when needed
            heapq.heappush(toPop, -1*A[i])
            while toPop and toPop[0] == maxHeap[0]:
                heapq.heappop(maxHeap)
                heapq.heappop(toPop)
            heapq.heappush(maxHeap, -1*A[i+k])

        res.append(-1*maxHeap[0])       # add the value of the last window
        return res

print(Solution().maxSlidingWindow([1,2,3,4,5], 3))
print(Solution().maxSlidingWindow([1,2,3,4,5,4,3,2,3,4,5,4,3,2], 3))