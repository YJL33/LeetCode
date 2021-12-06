from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return nums
        if len(nums) < 1+2*k: return [-1]*len(nums)
       
        res = []
        i = 0
        prevSum = None
        div = 1+2*k
        while len(res) < len(nums):
            l, r = i-k, i+k
            # subSum = sum(nums[l:r+1])
            if l < 0 or r >= len(nums):
                res.append(-1)
            else:
                if not prevSum:
                    subSum = sum(nums[l:r+1])
                else:
                    subSum = prevSum - nums[l-1] + nums[r]
                res.append(subSum//div)
                prevSum = subSum
            i += 1
        return res
