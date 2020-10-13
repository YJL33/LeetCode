"""
see https://leetcode.com/problems/my-calendar-i/
"""
import bisect
class MyCalendar(object):
    def __init__(self):
        self.meetings = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.checkOverlap(start, end):
            self.meetings += (start, end),
            self.meetings.sort()
            return True
        else:
            return False

    def checkOverlap(self, s, e):
        # search whether the incoming start time (s) is behind which end time
        # and see if the next start time happens earlier than the incoming end time (e)
        if not self.meetings:
            return True

        # search - can be optimized by bisect
        # self.meetings[o] will be the first meeting ends after s
        o = 0
        while o < len(self.meetings) and self.meetings[o][-1] <= s:
            o += 1

        if o < len(self.meetings):
            return self.meetings[o][0] >= e
        else:
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)