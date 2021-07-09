"""
526
"""
import random
import bisect
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.arr = [w[0]]
        for n in w[1:]:
            self.arr.append(self.arr[-1]+n)

    def pickIndex(self):
        """
        :rtype: int
        """
        rnd = random.random()*self.arr[-1]
        i = bisect.bisect_left(self.arr, rnd)
        return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()