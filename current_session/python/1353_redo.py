from typing import List
import heapq
# naive approach
# sort all events
# attend the early events first
# use a heap to store all events
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)      # pop from the tail
        minHeap = []
        cnt, day = 0, 0
        while minHeap or events:
            if not minHeap:                         # no event to attend...
                day = events[-1][0]                 # ...fast forward to the next event start day
            while events and events[-1][0] <= day:  # add all events start that day into heap
                heapq.heappush(minHeap, events.pop()[1])    # note that we add its end-day into heap
            heapq.heappop(minHeap)                  # attend one event (there must be one event available)
            cnt += 1                                # <KEY> attend one event per loop
            day += 1                                # move to next day
            while minHeap and minHeap[0] < day:     # purge stale events
                heapq.heappop(minHeap)

        return cnt