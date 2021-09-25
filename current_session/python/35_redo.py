# simply use binary search
import bisect
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # print(bisect.bisect_left(nums, target) == self.binarySearch(nums, target))
        return self.binarySearch(nums, target)


    # implement bisect
    def binarySearch(self, arr, target):
        if target <= arr[0]: return 0
        elif target > arr[-1]: return len(arr)

        l, r = 0, len(arr)-1
        while l < r:
            m = l + (r-l)//2
            if arr[m] < target:     # m is too small
                l = m+1
            else:                   # m is too big, at the left side
                r = m
        return l

print(Solution().searchInsert([1,3,5,6],5))
print(Solution().searchInsert([1,3,5,6],2))
print(Solution().searchInsert([1,3,5,6],7))
print(Solution().searchInsert([1,3,5,6],0))
print(Solution().searchInsert([1],0))
print(Solution().searchInsert([1],4))
        