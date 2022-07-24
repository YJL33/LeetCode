# release (empty) the room when the meeting is finished
# add one if there's no empty room

from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[int])->int:
        events = []
        for m in intervals:
            s, e = m[0], m[1]
            events.append((e, "e"))
            events.append((s, "s"))
        
        events.sort()
        # print("events:", events)
        roomCnt = 0
        emptyRoom = 0

        for e in events:
            if e[1] == "s":
                if emptyRoom > 0:
                    emptyRoom -= 1
                else:
                    roomCnt += 1
            else:
                emptyRoom += 1
        
        return roomCnt

print(Solution().minMeetingRooms([[0,30],[5,10],[15,20]]))
print(Solution().minMeetingRooms([[7,10],[2,4]]))