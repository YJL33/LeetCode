"""
https://leetcode.com/problems/design-hit-counter/
"""
import bisect
class HitCounter(object):

    # use a dict and keep count current sum
    # dct[t] = sum at time x

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cd = {}
        self.cd[0] = 0
        self.sum = 0
        
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.sum += 1
        if timestamp in self.cd:
            self.cd[timestamp] += 1
        else:
            self.cd[timestamp] = self.sum

    def getHits(self, t):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        #    t-300                  t
        # |---|-----|---------|-----|
        # h   h     h         h     h
        # 1   2     3         4     5
        ts = self.cd.keys()
        ts.sort()
        t1 = ts[-1]
        if t1 < t-300: return 0
        # i2 = bisect.bisect_left(ts, t-300)
        i2 = self.findT2(t, ts)
        # assert i2 == j2
        if t-300 not in self.cd: i2 = max(0, i2-1)
        t2 = ts[i2]
        
        return self.cd[t1] - self.cd[t2]

    def findT2(self, t1, ts):
        l, r = 0, len(ts)-1
        while l < r:
            m = l + (r-l)//2
            if ts[m] >= t1-300:
                r = m
            else:
                l = m+1
        return l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)