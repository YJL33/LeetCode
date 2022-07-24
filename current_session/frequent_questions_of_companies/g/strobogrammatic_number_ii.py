# strobogrammatic number
# n = 1: 1, 8, 0
# n = 2: 11, 88, 69, 96
# f(n) = add (n=2) at the both end of f(n-2)

from typing import List
class Solution:
    def findStrobogrammatic(self, n: int, needZero=False) -> List[str]:
        if n == 0: return [""]
        if n == 1: return ["1", "0", "8"]
        if n == 2: return ["11", "88", "69", "96"] if not needZero else ["11", "88", "69", "96", "00"]

        res = []
        base = self.findStrobogrammatic(n-2, True)
        twos = self.findStrobogrammatic(2, needZero)
        for x in base:
            for two in twos:
                res.append(two[0] + x + two[1])
        return res

print(Solution().findStrobogrammatic(1))
print(Solution().findStrobogrammatic(2))
print(Solution().findStrobogrammatic(3))