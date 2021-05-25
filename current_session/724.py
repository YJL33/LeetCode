"""
724
"""
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        rsum = [0 for _ in range(len(nums))]
        for j in range(len(nums)-2, -1, -1):
            rsum[j] = rsum[j+1]+nums[j+1]
        
        lsum = 0
        for i in range(len(nums)-1):
            if lsum == rsum[i]:
                return i
            lsum += nums[i]

        return -1 if lsum != rsum[-1] else len(rsum)-1
    
    def pivotIndex2(self, A: List[int]) -> int:
        l, r = 0, sum(A)-A[0]
        for i in range(len(A)-1):
            if l == r: return i
            l, r = l+A[i], r-A[i+1]
            
        return -1 if l != r else len(A)-1
            

print(Solution().pivotIndex2([1,7,3,6,5,6]))
print(Solution().pivotIndex2([1,2,3]))
print(Solution().pivotIndex2([2,1,-1]))
print(Solution().pivotIndex2([-1,-1,0,1,1,0]))
