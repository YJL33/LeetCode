"""
453
"""
from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # find the min value and sum the diff of A[i]-min
        minSeen, sd = min(nums), 0
        for i in range(len(nums)):
            sd += nums[i]-minSeen
        return sd


print(Solution().minMoves([1,2,3]))