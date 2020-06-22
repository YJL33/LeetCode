"""
MinHeap

Check the usage at #295
"""
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
        self.arr += num,
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

        # print mh.arr

# print MinHeap()
# mh = MinHeap()
# mh.push(5)
# mh.push(10)
# mh.push(3)
# mh.push(2)
# mh.push(1)
# print mh.arr
# print mh.pop()
# print mh.arr

