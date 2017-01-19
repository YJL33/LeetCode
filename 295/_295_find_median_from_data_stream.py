"""
295. Find Median from Data Stream

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.
Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
"""
from heapq import *        # In python the heap is a MIN heap

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []             # Stores the number that smaller than median, a max heap (* -1)
        self.large = []             # Stores the number that larger than median, a min heap
        self.size = 0               # Stores the size of data

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.small, (-1)*heappushpop(self.large, num))
        self.size += 1

        # Adjust the size of both heap,
        while len(self.large) < len(self.small):        # keep the large always slightly bigger
            heappush(self.large, (-1)*heappop(self.small))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.size%2:
            return float(self.large[0])
        else:
            return float(self.large[0] + (-1)*self.small[0])/2.0
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()