from typing import List
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        L = len(nums)
        def getDist(i):
            return i+1, L-i
        minSeen, maxSeen = -1, -1
        for i in range(len(nums)):
            if minSeen == -1 or nums[i] < nums[minSeen]:
                minSeen = i
            if maxSeen == -1 or nums[i] > nums[maxSeen]:
                maxSeen = i
        # print( nums[minSeen], nums[maxSeen])
        minDL, minDR = getDist(minSeen)
        maxDL, maxDR = getDist(maxSeen)
        return min(max(minDL, maxDL), max(minDR, maxDR), minDR+maxDL, minDL+maxDR)

print(Solution().minimumDeletions([2,10,7,5,4,1,8,6]))
print(Solution().minimumDeletions([0,-4,19,1,8,-2,-3,5]))
print(Solution().minimumDeletions([-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]))
# [101]