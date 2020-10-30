"""
see https://leetcode.com/problems/rle-iterator/
"""
class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.rpt = [a for a in A[::2]]
        self.num = [a for a in A[1::2]]
        self.pos = 0
        # print(self.rpt)
        # print(self.num)

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = self.pos
        while n:
            if i >= len(self.rpt):
                self.pos = i
                return -1
            if n-self.rpt[i] > 0:
                n, self.rpt[i] = n-self.rpt[i], 0
                i += 1
            else:
                n, self.rpt[i] = 0, self.rpt[i]-n

        self.pos = i
        # print(self.pos)

        return self.num[i]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)