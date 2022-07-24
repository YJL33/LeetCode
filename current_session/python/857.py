# min cost to hire k workers
# sort based on wage/quality ratio
# start from the most expensive one
# gruadually add cheaper one
# leverage the ratio, we can simply convert the overall wage from quality

from typing import List
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [(wage[i]/quality[i], quality[i]) for i in range(len(quality))]
        workers.sort()
        # print(workers)
        qSum = 0
        h = []
        res = float('inf')

        for r, q in workers:        # w[0]:ratio, w[1]:quality
            qSum += q
            heapq.heappush(h, -q)   # minHeap of quality
            if len(h) > k:          # pop first for evaluation
                qSum += heapq.heappop(h)
            if len(h) == k:
                res = min(res, r*qSum)
        return res
