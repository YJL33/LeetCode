from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if colors[0] == colors[-1]:
            r = len(colors)-1
            while r >= 0 and colors[r] == colors[0]:
                r -= 1
            if r == 0: return 0
            l = 0
            while l < len(colors) and colors[l] == colors[-1]:
                l += 1
            return max(0, r, len(colors)-1-l)
        else:
            return len(colors)-1