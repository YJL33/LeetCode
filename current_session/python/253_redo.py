"""
253
"""
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for m in intervals:
            s, e = m[0], m[1]
            events += (e, 'e'),
            events += (s, 's'),
        
        events.sort()       # sort by time, end before start
        emptyRoom, requiredRoom = 0, 0
        for e in events:
            if e[1] == 's':
                if emptyRoom == 0:
                    requiredRoom += 1
                else:
                    emptyRoom -= 1
            else:
                emptyRoom += 1
        
        return requiredRoom

print(Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(Solution().minMeetingRooms([[0, 30],[0,5],[5, 10],[10, 15],[15, 20]]))
print(Solution().minMeetingRooms([[7,10],[2,4]]))