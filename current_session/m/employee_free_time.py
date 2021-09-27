import heapq

# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        # convert all intervals to list
        scheduleHeap = []
        for i in range(len(schedule)):
            s, e = schedule[i], i
            for interval in s:
                heapq.heappush(scheduleHeap, (interval.start, 's', interval.end-interval.start))

        numOfEmployees = len(schedule)
        # at time == 0: everyone should be available
        availCnt = numOfEmployees
        prev = float('-inf')
        res = []
        while scheduleHeap:
            time, type, duration = heapq.heappop(scheduleHeap)
            if availCnt == numOfEmployees and type == 's':
                availCnt -= 1
                res.append([prev, time])
                prev = None
                heapq.heappush(scheduleHeap, (time+duration, 'e', None))
            elif type == 'e' and availCnt+1 == numOfEmployees:
                availCnt += 1
                prev = time
            elif type == 's':
                heapq.heappush(scheduleHeap, (time+duration, 'e', None))
                availCnt -= 1
            elif type == 'e':
                availCnt += 1

        return [Interval(s[0], s[1]) for s in res if s[0] != float('-inf') and s[0] != s[1]]
