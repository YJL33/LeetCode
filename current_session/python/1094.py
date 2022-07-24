# clarification
# dummy cases
# call-outs and optimizations
from typing import List
import heapq
class Solution:
    # idea: (simulation)
    # modify trips => (time, change of passenger), sort it and check capacity.
    # (no need for heap operation)
    # tc: O(NlogN) to sort, where N = 2n, O(N) to go through all trips
    # sc: additional O(N) to store new array
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, start, end in trips:
            events.append((start, num))
            events.append((end, -num))
        events.sort()
        caps = 0
        for _, diff in events:
            caps += diff
            if caps > capacity: return False
        return True
    # sort trips in-place
    # say we have first trip: num_of_passengers, start0, end0
    # collect all trips that has start time before end0
    # make all of them onboard, and check the capacity.
    # use a heap to maintain their drop location and drop them when needed.
    #
    # tc: 
    # O(nlogn) sort, 
    # O(n) to go through all trips, and O(logh) for heap operation, overall O(n)*O(logh)
    # sc:
    # O(h) to store heap
    def carPooling_2(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])       
        # print('trips:', trips)

        current_caps = 0
        removals = []
        i = 0
        while i < len(trips):
            j = i
            while j < len(trips) and trips[j][1] < trips[i][-1]:
                j += 1
            for k in range(i, j):
                num_of_onboard_passengers, start, end = trips[k]
                while removals and removals[0][0] <= start:
                    _, num_off = heapq.heappop(removals)
                    current_caps -= num_off
                current_caps += num_of_onboard_passengers
                if current_caps > capacity:
                    return False
                heapq.heappush(removals, (end, num_of_onboard_passengers))
            i = j
        return True
