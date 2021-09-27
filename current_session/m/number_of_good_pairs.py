from typing import List
import collections

# use mergesort
# while merging L and R, if any L < R: cnt += 1
# O(nlogn)

# ... or we can simply count the appearences, and then
# e.g. by observation:
# appearences = 2 => pairs = 1
# appearences = 3 => pairs = 3
# appearences = 4 => pairs = 6
# ...
# directly return the value
# time analysis: O(n)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        res = 0
        for k, v in cnt.items():
            if v >= 2:
                res += self.helper(v)
        return res
    
    def helper(self, n):
        return int((n)*(n-1)*0.5)

print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution().numIdenticalPairs([1,1,1,1]))
print(Solution().numIdenticalPairs([1,2,3]))