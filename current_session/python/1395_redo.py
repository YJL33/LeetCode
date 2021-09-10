# for each number i, count:
# 1. all j that j<i and A[j]<A[i]
# 2. all j that j<i and A[j]>A[i]
# 3. all k that k>i and A[k]<A[i]
# 4. all k that k>i and A[k]>A[i]
# teams that using i as center = 1*4+2*3
# use minHeap and maxHeap
from typing import List
import heapq
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        L = len(rating)
        ll, lg, rl, rg = [0],[0],[0],[0]

        # minHeap: everything in this heap is bigger than target
        # maxHeap: vice versa
        minH, maxH = [], []
        for i in range(L-1):
            j = i+1
            # add i into heaps and adjust the heaps
            heapq.heappush(minH, rating[i])
            l, g = self.adjustHeaps(minH, maxH, rating[j])
            ll.append(l)
            lg.append(g)
        # print('ll:', ll, 'lg:', lg)

        minH, maxH = [], []
        for i in range(L-1,0,-1):
            j = i-1
            heapq.heappush(minH, rating[i])
            l, g = self.adjustHeaps(minH, maxH, rating[j])
            rl.append(l)
            rg.append(g)
        # print('rl:', rl, 'rg:', rg)

        return sum([ll[i]*rg[~i] + lg[i]*rl[~i] for i in range(L)])
    
    def adjustHeaps(self, minH, maxH, target):
        while minH and minH[0] <= target:
            x = heapq.heappop(minH)
            heapq.heappush(maxH, -1*x)
        while maxH and -1*maxH[0] >= target:
            x = heapq.heappop(maxH)
            heapq.heappush(minH, -1*x)
        return len(maxH), len(minH)

print(Solution().numTeams([2,5,3,4,1]))
