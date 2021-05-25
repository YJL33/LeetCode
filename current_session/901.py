"""
901
"""
from typing import List
class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        # keep add to arr if decreasing, pop if increasing
        cnt = 1
        while self.arr and self.arr[-1][0] <= price:
            cnt += self.arr.pop()[1]
        self.arr.append([price, cnt])
        return cnt
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
