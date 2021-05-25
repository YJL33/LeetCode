"""
354
"""
import bisect
class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        # sort by height
        # if same height, put higher width in front
        # find Longest Increasing Sequence (by width)
        A.sort(key=lambda x:(x[0], -x[1]))
        lis = []
        for i in range(len(A)):
            b = bisect.bisect_left(lis, A[i][1])
            if b >= len(lis):
                lis += A[i][1],
            else:
                lis[b] = A[i][1]
        
        return len(lis)

print(Solution().maxEnvelopes([[6, 4], [6, 7], [5, 4], [2, 3]]))