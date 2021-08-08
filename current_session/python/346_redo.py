class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nsum = 0
        self.arr = [0 for _ in range(size)]
        self.ncnt = 0

    def next(self, val: int) -> float:
        self.nsum += val
        self.nsum -= self.arr[self.ncnt%self.size]
        self.arr[self.ncnt%self.size] = val
        self.ncnt += 1
        return 1.0*(self.nsum)/(self.size if self.ncnt>self.size else self.ncnt)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)