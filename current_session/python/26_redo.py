from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # simply use 2 pointers
        # go through the whole array and track the next filling position
        i, j = 0, 0
        # find the next unique number and assign it into the next filling position
        while i < len(nums) and j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j < len(nums):
                i += 1                  # next filling position
                nums[i] = nums[j]       # assign it
        
        return i+1