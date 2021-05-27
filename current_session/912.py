"""
912
"""
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            i, j = 0, 0
            arr = []
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    arr += l[i],
                    i += 1
                else:
                    arr += r[j],
                    j += 1
            while i < len(l):
                arr += l[i],
                i += 1
            while j < len(r):
                arr += r[j],
                j += 1
            return arr
        # merge sort
        if len(nums) == 1: return nums
        L = len(nums)
        left, right = self.sortArray(nums[L//2:]), self.sortArray(nums[:L//2])
        return merge(left, right)

print(Solution().sortArray([5,2,3,1]))
print(Solution().sortArray([5,1,1,2,0,0]))