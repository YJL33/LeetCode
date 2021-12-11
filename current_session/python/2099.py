from typing import List
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # simply use a heap
        if k == len(nums):
            return nums
        hp = []
        for i in range(len(nums)):
            heapq.heappush(hp, (-1*nums[i], i))
        
        indexes = []
        while len(indexes) < k:
            _, b = heapq.heappop(hp)
            indexes.append(b)
        
        indexes.sort()
        
        return [nums[i] for i in indexes]
