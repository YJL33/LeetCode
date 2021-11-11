from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSeen = float('inf')
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            minSeen = min(minSeen, prefixSum)
        
        if minSeen > 0:
            return 1
        else:
            return (-1*minSeen)+1

print(Solution().minStartValue([-3,2,-3,4,2]))
print(Solution().minStartValue([1,2]))
print(Solution().minStartValue([1,-2,-3]))