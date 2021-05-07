"""
1525
"""
from typing import List
import collections
class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) <= 1: return 0
        cl, cr = collections.Counter(""), collections.Counter(s)
        res = 0
        for i in range(len(s)):
            x = collections.Counter(s[i])
            cl, cr = cl+x, cr-x
            if len(cl) == len(cr):
                # print('l, r', s[:i+1], s[i+1:])
                # print('cl, cr', cl, cr)
                res += 1
        return res
            
print(Solution().numSplits("aacaba"))