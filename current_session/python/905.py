from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # similar to quicksort partition
        # find odd-even pairs and swap them
        left, right = 0, len(nums)-1
        while left <= right:
            while left < len(nums) and nums[left]%2 == 0:
                left += 1
            while right >= 0 and nums[right]%2 == 1:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1
        return nums

    def sortArrayByParity_2(self, nums: List[int]) -> List[int]:
        # similar to quicksort - pivot partition
        idx = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return nums
