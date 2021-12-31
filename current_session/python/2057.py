from typing import List
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            if n == i%10:
                return i
        return -1
        