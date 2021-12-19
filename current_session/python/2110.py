from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # use monotonic stack
        # if decreasing: add into it
        # else:
        # close previous one
        # start from one
        ms = []
        cnt = 0

        def count(arr):
            # e.g. len(arr) == 3 => (3+1)*3/2
            return 0.5*len(arr)*(len(arr)+1)
        for i in range(len(prices)):
            p = prices[i]
            if not ms or ms[-1] != p+1:
                # close previous one
                cnt += count(ms)
                ms = [p]
            else:
                assert(ms[-1] == p+1)
                ms.append(p)
        
        if ms: cnt += count(ms)
        return int(cnt)