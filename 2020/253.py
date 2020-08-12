"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019.
Please reset to default code definition to get new method signature.
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort the "meeting start" and "meeting end" events
        # +1 room if all room not finished yet
        # go next if has empty room
        # time: O(nlogn)
        # space O(n)

        meetingEvents = []

        for interval in intervals:
            meetingEvents += (interval[0], "s"),
            meetingEvents += (interval[1], "e"),

        meetingEvents.sort()        # note that "e" < "s"

        emptyRoom, neededRoom = 0, 0

        for i in xrange(len(meetingEvents)):
            if meetingEvents[i][1] == "s":
                if emptyRoom == 0:
                    neededRoom += 1
                else:
                    emptyRoom -= 1
            else:
                emptyRoom += 1

        return neededRoom

print Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]])
print Solution().minMeetingRooms([[0, 30],[0,5],[5, 10],[10, 15],[15, 20]])
print Solution().minMeetingRooms([[7,10],[2,4]])