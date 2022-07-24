# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # clarification
        # inclusive/exclusive?
        # 
        # thoughts
        # concatenate all schedule?
        # handle based on 'event time' (T start-working,  T end-working)
        # sort all events
        # if we see everyone is available: we have common_free_start
        # the next one breaks the status: add [common_free_start, T]
        # 
        # so on and so forth
        #
        N, events = len(schedule), []
        for employee, sc in enumerate(schedule):
            for intvl in sc:
                events.append((intvl.start, 'b', employee))
                events.append((intvl.end, 'e', employee))

        events.sort()
        # is_available = [True for _ in range(len(schedule))]     # whether all employees are available
        avail_cnt = N
        
        common_free = None
        res = []
        for t, evnt_type, i in events:
            if evnt_type == 'b':
                avail_cnt -= 1
            else:
                avail_cnt += 1
            
            if avail_cnt == N:
                common_free = t
            elif common_free:
                res.append(Interval(common_free, t))
                common_free = None
        
        return res