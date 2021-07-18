"""
1578
"""
from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        minCost = 0
        prevI, cur = 0, 0
        for i in range(1,len(s)):
            if s[i] == s[prevI]:
                cur = i
            else:
                if cur != prevI:
                    minCost += sum(cost[prevI:i]) - max(cost[prevI:i])
                cur = i
                prevI = i
            # print('i',i,'minCost',minCost)
        if cur != prevI: minCost += sum(cost[prevI:]) - max(cost[prevI:])
        return minCost

print(Solution().minCost("abaac",[1,2,3,4,5]))
print(Solution().minCost("abc",[1,2,3]))
print(Solution().minCost("aabaa",[1,2,3,4,1]))