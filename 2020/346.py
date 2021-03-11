"""
346
"""
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.arr = [None for _ in range(size)]
        self.tot = 0
        self.cnt = 0
        self.size = size

    def next(self, val: int) -> float:
        self.cnt += 1
        i = self.cnt%self.size
        if self.cnt > self.size:
            self.tot = self.tot - self.arr[i]
        self.arr[i] = val
        self.tot += val
        if self.cnt >= self.size:
            return (self.tot*1.0)/self.size
        else:
            return (self.tot*1.0)/self.cnt
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)