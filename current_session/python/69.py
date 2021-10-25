class Solution:
    def mySqrt(self, x: int) -> int:
        # use binary search
        # search range: from 1 to (x-1)
        if x <= 1: return x
        l, r = 1, x-1
        while l <= r:
            m = (l+r)//2
            if m*m <= x and (m+1)*(m+1) > x:
                return m
            elif m*m > x:       # sqrt is smaller
                r = m-1
            else:
                l = m+1
        return -1
