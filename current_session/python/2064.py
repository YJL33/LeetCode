from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search
        # all products needs to be distributed
        N = sum(quantities)
        l, r = (N//n)+(1 if N%n else 0), N-(n-1)

        def canDistribute(x):
            cnt = 0
            dist = [q for q in quantities]
            for i in range(len(dist)):
                cnt += (dist[i]//x) + (1 if dist[i]%x else 0)
            return cnt <= n

        while l < r:
            m = (l+r)//2
            if canDistribute(m):        # find smaller one
                r = m
            else:                       # seek bigger x
                l = m+1
        return l

