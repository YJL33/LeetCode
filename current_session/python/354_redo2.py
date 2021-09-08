from typing import List
import bisect
class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        if not A: return 0
        # each envelope [w, h], only w1 and h1 are both greater than w2 and h2 will fit
        # sort the envelope by width, if same width, bigger height comes first
        # then find the longest increasing sequence of height
        A.sort(key=lambda x:(x[0], -x[1]))
        lis = []
        for a in A:
            b = bisect.bisect_left(lis, a[1])
            if b >= len(lis):
                lis.append(a[1])
            else:
                lis[b] = a[1]
        return len(lis)

print(Solution().maxEnvelopes([[6, 4], [6, 7], [5, 4], [2, 3]]))