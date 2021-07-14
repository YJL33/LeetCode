"""
85
"""
from typing import List

class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        # for each "row", find max histogram
        # O(NM)
        if not mat: return 0
        hist = [[1 if x == '1' else 0 for x in row] for row in mat]
        for i in range(1,len(hist)):
            for j in range(len(hist[0])):
                if hist[i][j] == 1: hist[i][j] += hist[i-1][j]
        # print(hist)

        def helper(hist):
            # O(n) to find biggest histogram
            hist += 0,
            st = []
            zeroIndex = -1          # handle edge case
            maxSeen = 0
            for i in range(len(hist)):
                while st and hist[st[-1]] > hist[i]:
                    h = hist[st.pop()]
                    prevI = zeroIndex if not st else st[-1]
                    w = i-(prevI+1)
                    maxSeen = max(maxSeen, h*w)
                st.append(i)
            return maxSeen

        # print([helper(h) for h in hist])
        return max([helper(h) for h in hist])
