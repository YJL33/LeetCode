from typing import List
class Solution:
    def findPeakElement_linear(self, A: List[int]) -> int:
        # linear: time O(N)
        prev = 0
        for i in range(1,len(A)):
            if A[prev] > A[i]:
                return prev
            else:
                prev = i
        return prev

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[~0] > nums[~1]: return len(nums)-1
        
        def is_peak(mid):
            return nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]
        
        # use binary search: time O(logN)
        l, r = 1, len(nums)-2
        while l <= r:
            mid = (l+r)//2
            if is_peak(mid):
                return mid
            elif nums[mid]<nums[mid+1]:     # search the right side
                l = mid+1
            else:
                r = mid-1
        return -1