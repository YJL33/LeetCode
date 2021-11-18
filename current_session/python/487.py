from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        globalMax = 0
        maxCntNoFlip, maxCntFlipped = 0, 0
        # a, b = [], []
        for i in range(len(nums)):
            if nums[i] == 0:
                maxCntFlipped, maxCntNoFlip = max(maxCntNoFlip+1, 1), 0
                
            else:
                maxCntFlipped, maxCntNoFlip = maxCntFlipped+1, maxCntNoFlip+1
            # a += maxCntFlipped,
            # b += maxCntNoFlip,
            # print('a', a)
            # print('b', b)
            globalMax = max(globalMax, maxCntFlipped, maxCntNoFlip)
        return globalMax

print(Solution().findMaxConsecutiveOnes([1,0,1,1,0]))
print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))
