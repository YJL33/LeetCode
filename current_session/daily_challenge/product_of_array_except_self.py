from typing import List
class Solution:
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use something like prefix sum
        left, right = [1 for _ in nums], [1 for _ in nums]
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i]
            right[~i] = right[~(i-1)]*nums[~i]
        
        res = [1 for _ in nums]
        for i in range(len(nums)):
            l = left[i-1] if i-1 >= 0 else 1
            r = right[i+1] if i+1 < len(nums) else 1
            res[i] = l*r
        
        return res
        """
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        overall = 1
        zeroCnt, zeroIndex = 0, -1
        for i in range(len(nums)):
            n = nums[i]
            if n == 0 and zeroCnt < 1:
                zeroCnt, zeroIndex = 1, i
            elif n == 0 and zeroCnt == 1:
                return [0 for _ in nums]
            else:
                overall *= n
        
        if zeroCnt:
            res = [0 for _ in nums]
            res[zeroIndex] = overall
        else:
            res = []
            for n in nums:
                res.append(overall//n)
        return res

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1,1,0,-3,3]))