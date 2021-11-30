from typing import List
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # from L->R, and from R->L
        l1, l2, l3 = -1, -1, -1
        r1, r2, r3 = -1, -1, -1
        L = len(colors)
        left = [None for _ in range(L)]
        right = [None for _ in range(L)]
        for i in range(L):
            c, d = colors[i], colors[~i]            # ~i == L-1-i
            if c == 1:
                l1 = i
            elif c == 2:
                l2 = i
            else:
                l3 = i
            if d == 1:
                r1 = L-1-i
            elif d == 2:
                r2 = L-1-i
            else:
                r3 = L-1-i
            left[i] = (l1, l2, l3)
            right[~i] = (r1, r2, r3)
        res = []
        for i, tgt in queries:
            ll, rr = left[i][tgt-1], right[i][tgt-1]
            minDist = float('inf')
            if ll != -1: minDist = min(minDist, i-ll)
            if rr != -1: minDist = min(minDist, rr-i)
            res.append(minDist if minDist != float('inf') else -1)

        return res

print(Solution().shortestDistanceColor([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]))
print(Solution().shortestDistanceColor([1,2], [[0,3]]))