from typing import List
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(p)
        cntp = collections.Counter(p)
        cntx = collections.Counter(s[:N])
        res = []
        if cntp == cntx: res.append(0)
        for i in range(1,len(s)-N+1):
            cntx[s[i-1]] -= 1
            cntx[s[i+N-1]] += 1
            if cntx == cntp:
                res.append(i)
        return res