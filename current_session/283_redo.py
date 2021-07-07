"""
283
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        L = len(nums)
        while i < L:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                L -= 1
            else:
                i += 1
        return