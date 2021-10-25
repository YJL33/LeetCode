from typing import List
import heapq
import timeit
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # use min Heap (TLE)
        # for n workers, calculate the distance to all bikes (pair to all of them)
        # and put it into min (distance) heap
        # return the optimal pairing
        # analysis: O(n*m) for all pairing, O(PlogP) for heap operation, where P is the number of pairing (n*m/2)

        # t = timeit.Timer()

        h = []      # cost heap, arrange workers from 0-n, seen bikes (using bitwise to check the bike is used or not)
        h.append([0,0,0])           # start from 0-th worker (to be assigned)
        seen = set()

        def dis(i, j): return abs(workers[i][0]-bikes[j][0]) + abs(workers[i][1]-bikes[j][1])

        while h:
            cost, worker, takenBikes = heapq.heappop(h)

            # to avoid a1-b1, a2-b2 <-> a1-b2, a2-b1 this kind of paring
            # where the better one should appear first
            if (worker, takenBikes) in seen: continue
            seen.add((worker, takenBikes))

            if worker == len(workers):
                # print('t:', t.timeit())
                return cost          # the optimal answer
            for j in range(len(bikes)):
                if (takenBikes & (1<<j)) == 0:              # never use this bike, add it
                    heapq.heappush(h, [cost+dis(worker, j), worker+1, takenBikes | (1<<j)])

print(Solution().assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]],[[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999]]))
