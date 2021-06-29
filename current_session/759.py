"""
759
"""
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        # collect all 'events'
        events = []
        for i in range(len(schedule)):
            es = schedule[i]    # employee schedule
            for j in range(len(es)):
                s, e = es[j].start, es[j].end
                events.append((e, 'e', i))      # 'e' < 's'
                events.append((s, 's', i))
        events.sort()
        # print('evnts:',events)
        currentTime = events[0][0]
        res, tmp = [], ['-inf']
        n, availableCnt = len(schedule), len(schedule)
        i = 0
        # print('n', n)
        while i < len(events):
            while i < len(events) and events[i][0] == currentTime:
                time, delta, _ = events[i]
                availableCnt = availableCnt+1 if delta == 'e' else availableCnt-1
                i += 1
            # print('i, a, tmp', i, availableCnt, tmp)
            if availableCnt != n and len(tmp):
                # tmp += currentTime,
                res += Interval(tmp[0], currentTime),
                tmp = []
            elif availableCnt == n and not tmp:
                tmp = [currentTime]
            # print('res:',[[r.start, r.end] for r in res])
            if i< len(events): currentTime = events[i][0]
            
        
        return res[1:]