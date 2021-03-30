"""
1578
"""
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        prev, i = 0, 1
        c = 0
        while i < len(s):
            while i < len(s) and s[i] == s[prev]:
                i += 1
            if s[i-1] == s[prev] and i-prev > 1:
                c += sum(cost[prev:i]) - max(cost[prev:i])
            prev, i = i, i+1
        return c