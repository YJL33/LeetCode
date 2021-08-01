from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, [], 0)
        return self.res
    def helper(self, nums, tmp, start):
        self.res += tmp,
        for i in range(start, len(nums)):
            self.helper(nums, tmp+[nums[i]], i+1)
        return