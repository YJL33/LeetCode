from typing import List
import heapq
import collections
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        N, M = len(workers), len(bikes)
               
        def getDist(i1, j1, i2, j2):
            return abs(i1-i2)+abs(j1-j2)
        
        wd = collections.defaultdict(list)          # key: worker , value: heap of min-distance to bikes
        for n in range(N):
            for m in range(M):
                heapq.heappush(wd[n], (getDist(workers[n][0], workers[n][1], bikes[m][0], bikes[m][1]), m))

        minHeap = []                                # store (dist, worker, bike) of all workers, top-priorities only
        for n in range(N):
            dist, top_priority_bike = heapq.heappop(wd[n])
            heapq.heappush(minHeap, (dist, n, top_priority_bike))
        
        res = [-1 for _ in range(N)]
        occupiedBike = set()
        
        while minHeap:
            dist, w, b = heapq.heappop(minHeap)
            if b in occupiedBike:
                while wd[w][0] in occupiedBike:
                    heapq.heappop(wd[w])
                dist, top_priority_bike = heapq.heappop(wd[w])
                heapq.heappush(minHeap, (dist, w, top_priority_bike))
            else:
                res[w] = b
                occupiedBike.add(b)

        return res