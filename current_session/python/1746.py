from typing import List
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        # naive approach
        # subarray can be partial

        globalMaxSum = float('-inf')
        localMaxSumNoFlip, localMaxSumFlipped = 0, 0
        a, b= [],[]
        for i in range(len(nums)):
            localMaxSumNoFlip, localMaxSumFlipped = max(localMaxSumNoFlip+nums[i], nums[i]), max(localMaxSumNoFlip+(nums[i]*nums[i]), localMaxSumFlipped+nums[i], (nums[i]*nums[i]))
            a.append(localMaxSumNoFlip)
            b.append(localMaxSumFlipped)
            # print('a',a)
            # print('b',b)
            globalMaxSum = max(localMaxSumFlipped, localMaxSumNoFlip, globalMaxSum)
        return globalMaxSum

print(Solution().maxSumAfterOperation([2,-1,-4,-3]))
print(Solution().maxSumAfterOperation([1,-1,1,1,-1,-1,1]))