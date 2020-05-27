"""
346. Moving Average from Data Stream

    Total Accepted: 8147
    Total Submissions: 14463
    Difficulty: Easy

Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

For example ... (refer to leetcode)
"""
import collections
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = 0.0
        self.maxsize = size
        self.sum = 0.0
        self.queue = collections.deque()
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size == self.maxsize:
            self.sum += float(val) - self.queue.popleft()     
        elif self.size < self.maxsize:
            self.size += 1.0
            self.sum += float(val)
        self.queue.append(val)
        return self.sum/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)