from typing import List
import bisect
class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        if not A: return 0
        # sort A by height, if same height bigger width come first
        A.sort(key=lambda x:(x[0],-x[1]))
        # see https://en.wikipedia.org/wiki/File:LISDemo.gif
        h = []
        for i, e in enumerate(A, 0):
            j=bisect.bisect_left(h, e[1])
            if j<len(h):        # directly update the LIS
                h[j]=e[1]
            else:               # increase the LIS
                h.append(e[1])
        return len(h)

print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
# print(Solution().maxEnvelopes([[1,1], [1,1], [1,1]]))
