"""
295. Find Median from Data Stream

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
# from heapq import *        # In python the heap is a MIN heap
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = MinHeap()
        self.large = MinHeap() # keep this slightly bigger than small
        self.size = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # heappush(self.small, (-1)*heappushpop(self.large, num))
        self.large.push(num)
        self.small.push((-1)*self.large.pop())
        self.size += 1

        while self.large.size() < self.small.size():
            self.large.push((-1)*self.small.pop())
            # heappush(self.large, (-1)*heappop(self.small))

    def findMedian(self):
        """
        :rtype: float
        """
        if self.size % 2:
            return float(self.large.peek())
        else:
            return float(self.large.peek() + (-1)*self.small.peek())/2

class MinHeap(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = [0]        # use self.arr[0] = empty for easier implementation
        
    def size(self):
        return len(self.arr)

    def peek(self):
        return self.arr[1]

    def push(self, num):
        """
        :type num: int
        :rtype: None
        """
        # add the number to the end, and percolate the rest.
        self.arr += [num]
        self.percolateUp(len(self.arr)-1)        

    def pop(self):
        """
        :rtype: int
        """
        # swap the first and last element, pop, and percolate the rest

        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        minVal = self.arr.pop()
        self.percolateDown(1)

        return minVal


    def percolateDown(self, i):
        j = 2*i
        # percolate down
        while j < len(self.arr):
            if j+1 < len(self.arr) and self.arr[j+1] < self.arr[j]:
                j += 1
            if self.arr[i] > self.arr[j]:
                self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
                i, j = j, 2*j
            else:
                break

    def percolateUp(self, i):
        h = i // 2
        # percolate down
        while self.arr[h] > self.arr[i] and h != 0:
            self.arr[h], self.arr[i] = self.arr[i], self.arr[h]
            i, h = h, h // 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()