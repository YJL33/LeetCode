"""
18
"""
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # leverage 3sum ~O(n) and 2sum O(n)
        # if we sort then things will be easier
        if len(nums) < 4: return []
        elif len(nums) == 4: return [] if sum(nums) != target else [nums]
        self.res = set()
        nums.sort()
        if sum(nums[:4]) > target or sum(nums[-4:]) < target: return
        for i in range(len(nums)):
            self.threeSum(nums[i+1:], target-nums[i], [nums[i]])
        return [[a,b,c,d] for a,b,c,d in self.res]
    
    def threeSum(self, nums, threeSumTgt, carry):
        # print('3sum')
        if len(nums) < 3: return
        elif sum(nums[:3]) > threeSumTgt or sum(nums[-3:]) < threeSumTgt: return
        for i in range(len(nums)):
            self.twoSum(nums[i+1:], threeSumTgt-nums[i], carry+[nums[i]])
        return
    
    def twoSum(self, nums, twoSumTarget, carry):
        # print('carry:', carry)
        if len(nums) < 2: return
        seen = {}
        tmp = []
        for i in range(len(nums)):
            if twoSumTarget-nums[i] in seen:
                tmp += [nums[i], nums[seen[twoSumTarget-nums[i]]]],
            else:
                seen[nums[i]] = i
        for x in tmp:
            a,b,c,d = carry+x
            self.res.add((a,b,c,d))
        return

# print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(Solution().fourSum([-1,0,1,2,-1,-4],-1))
