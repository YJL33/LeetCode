from typing import List
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # i: increase / d: decrease
        low, high = 0, len(s)
        res = []
        for i in range(len(s)):
            if s[i] == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        # assert(low==high)
        res.append(low)
        return res

print(Solution().diStringMatch("IDID"))
print(Solution().diStringMatch("III"))
print(Solution().diStringMatch("DDI"))
print(Solution().diStringMatch("DDD"))