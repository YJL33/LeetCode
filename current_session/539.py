"""
539
"""
from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert all time using minutes
        ts = []
        for t in timePoints:
            ts.append(self.getTime(t))
        
        ts.sort()
        # print('ts',ts)
        res = float('inf')
        prev = ts[-1]
        for t in ts:
            res = min(res, self.getDiff(prev, t))
            prev = t
        return res
    
    def getTime(self, t):
        H = int(t[0])*10 + int(t[1])
        M = int(t[3])*10 + int(t[4])
        return 60*H + M
    def getDiff(self, a, b):
        if a > b: b += 1440
        return b-a

print(Solution().findMinDifference(["00:00","23:59","00:00"]))
print(Solution().findMinDifference(["23:59","00:00"]))