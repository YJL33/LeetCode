import itertools
from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        perm = itertools.permutations([str(x) for x in digits], 3)
        res = set()
        for c in perm:
            y = int(''.join(c))
            if y%2 == 0 and y >= 100:
                res.add(y)
        ans = [x for x in res]
        ans.sort()
        return ans

print(Solution().findEvenNumbers([2,1,3,0]))
print(Solution().findEvenNumbers([2,2,8,8,2]))
print(Solution().findEvenNumbers([4,7,5]))
print(Solution().findEvenNumbers([0,2,0,0]))