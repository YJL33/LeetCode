'''
283
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        cnt = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                cnt += 1
            else:
                i += 1
        
        while cnt:
            nums.append(0)
            cnt -= 1
        return