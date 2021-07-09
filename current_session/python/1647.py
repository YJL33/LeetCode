"""
1647
"""
import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        ld = collections.Counter(s)
        x = sorted([v for v in ld.values()], reverse=True)
        prev, cnt = 0, 0
        seen = set(x)
        # print(x)
        for i in range(1,len(x)):
            if x[i] == x[prev]:     # need to delete until no same frequency
                val = x[i]
                while val in seen and val > 0:
                    val -= 1
                    cnt += 1
                if val > 0:
                    seen.add(val)
            prev = i
        return cnt
