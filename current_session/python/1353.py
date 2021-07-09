"""
1353
"""
from typing import List
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        cnt, day, minHeap = 0,0,[]
        while events or minHeap:
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

print('ANS:', Solution().maxEvents([[1,2],[2,3],[3,4]]), 'should be 3')
print('ANS:', Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]]), 'should be 4')
print('ANS:', Solution().maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]), 'should be 4')
print('ANS:', Solution().maxEvents([[1,100000]]), 'should be 1')
print('ANS:', Solution().maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]), 'should be 7')
print('ANS:', Solution().maxEvents([[1,10],[2,2],[2,2],[2,2],[2,2]]), 'should be 2')
print('ANS:', Solution().maxEvents([[1,2],[1,2],[1,6],[1,2],[1,2]]), 'should be 3')