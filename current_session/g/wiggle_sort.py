from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # simply swap if it's not right:
        # e.g. [3,2,1] -> [2,3,1]
        # looking for greater
        lfg = True
        for i in range(len(nums)):
            if i+1 == len(nums):
                return
            if (lfg and nums[i] > nums[i+1]) or (not lfg and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            lfg = not lfg
        return
