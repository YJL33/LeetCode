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

Follow up:
What if the number of hits per second could be very large? Does your design scale? 
"""
import collections
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cur = 1
        self.hitnum = [[]]*301      # put each sec as a queue

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)