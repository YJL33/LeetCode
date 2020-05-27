"""
362. Design Hit Counter

    Total Accepted: 4513
    Total Submissions: 9004
    Difficulty: Medium

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity),
and you may assume that calls are being made to the system in chronological order
(ie, the timestamp is monotonically increasing).

You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);

Follow up:
What if the number of hits per second could be very large? Does your design scale? 
"""
import heapq
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # implement Heap. Record number of hits in each second (count them and then add at once).
        self.minhp = []
        self.now = 0
        self.nowHits = 0
        self.hits = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if timestamp == self.now:
            self.nowHits += 1
        else:
            heapq.heappush(self.minhp, (self.now, self.nowHits))
            self.hits += self.nowHits
            self.now, self.nowHits = timestamp, 1
        # print self.minhp
        return

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.minhp and self.minhp[0][0] <= timestamp-300:
            # print self.minhp[0]
            self.hits -= heapq.heappop(self.minhp)[1]
        return self.hits+self.nowHits if self.now > timestamp-300 else self.hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)