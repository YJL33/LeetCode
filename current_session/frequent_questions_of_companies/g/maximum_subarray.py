# simply use greedy
# update localSum and globalSum

from typing import List
class Solution:
    def maxSubArray(self, nums:List[int]) -> int:
        localSum, globalSum = float('-inf'), float('-inf')
        for n in nums:
            localSum = max(localSum+n, n)
            globalSum = max(globalSum, localSum)
        return globalSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([5,4,-1,7,8]))
