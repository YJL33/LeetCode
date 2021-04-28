"""
1229
"""
from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # merge both slot and sort both slots and check from the beginning

        merged = [(a[0], a[1], 'A') for a in slots1] + [(b[0], b[1], 'B') for b in slots2]
        merged.sort(key=lambda x: x[0])

        # check one by one
        prev = None
        i = 0
        for i in range(len(merged)):
            if merged[i][1]-merged[i][0] < duration:        # next
                continue
            if not prev or merged[i][-1] == prev[-1]:       # update prev
                prev = merged[i]
                continue
            else:                                           # check timespan for both team
                res = self.isValid(prev, merged[i], duration)
                if res:
                    return res
                else:
                    prev = merged[i]
        return []
    
    def isValid(self, a, b, t):
        start = max(a[0], b[0])
        end = start+t
        if end <= a[1] and end <= b[1]:
            return [start, end]
        else:
            return False

print(Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))