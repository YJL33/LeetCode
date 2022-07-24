from typing import List
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findMin(nums)
        # print('pivot',pivot)
        start, end, add = 0, len(nums), 0
        if pivot != 0:
            if target > nums[-1]:
                end = pivot
            else:
                start, add = pivot, pivot
        i = bisect.bisect_left(nums[start:end], target) + add
        return i if i<len(nums) and nums[i] == target else -1

    def findMin(self, nums: List[int]) -> int:
        # simply use binary Search
        def binarySearch(A):
            l, r = 0, len(A)-1
            while l < r:
                m = l + (r-l)//2
                if A[m-1]>=A[m] and A[m]<=A[-1]: return m
                elif A[m] > A[0]: l = m+1
                elif A[m] < A[-1]: r = m
                else:
                    print("???")
            return l
        
        if len(nums) == 1: return 0
        elif len(nums) == 2: return 0 if nums[0] < nums[1] else 1

        return binarySearch(nums) if nums[0] > nums[-1] else 0
