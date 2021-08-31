# DP
# O(N) method: use bisect and keep update all possible lengths
#
import bisect
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [[nums[0]]]
        for n in nums[1:]:
            i = bisect.bisect_left([r[-1] for r in res], n)
            if i == len(res):
                res.append(res[-1]+[n])
            else:
                res[i][-1] = n
        return len(res[-1])

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
