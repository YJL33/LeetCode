from typing import List
from itertools import chain, combinations
class Solution:

    def powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))    

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # get the max possible bitwise OR
        L = len(nums)
        max_possible = nums[0]
        for n in nums[1:]:
            max_possible = max_possible | n
        
        # print('max', max_possible)
        self.cnt = 0
        possibilities = list(self.powerset(nums))
        # print('pos', possibilities)
        def get_val(p):
            if not p: return 0
            x = p[0]
            for y in p[1:]: x |= y
            return x
        for p in possibilities:
            if get_val(p) == max_possible: self.cnt += 1
        
        return self.cnt

print(Solution().countMaxOrSubsets([3,1]))
print(Solution().countMaxOrSubsets([2,2,2]))
print(Solution().countMaxOrSubsets([3,2,1,5]))