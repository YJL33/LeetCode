from typing import List
import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        seen = {}
        # find all factors of x
        def helper(x):
            res = []
            res.append([x])
            for a in range(2, int(math.sqrt(x))+1):
                if x%a == 0 and a <= x//a:
                    if x//a not in seen:
                        seen[x//a] = helper(x//a)
                    tmp = seen[x//a]
                    for t in tmp:
                        if t[0] < a: continue
                        res.append([a]+t)
            seen[x] = res
            return res

        if n == 1: return []

        listOfFactors = helper(n)
        return [list(l) for l in listOfFactors if len(l) != 1]

print(Solution().getFactors(1))
print(Solution().getFactors(7))
print(Solution().getFactors(8))
print(Solution().getFactors(12))
print(Solution().getFactors(15))
print(Solution().getFactors(32))
print(Solution().getFactors(33))
print(Solution().getFactors(37))
print(Solution().getFactors(9748778))
print(Solution().getFactors(8388608))