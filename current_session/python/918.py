from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # circular: use overall sum - minSubarraySum
        local_max = global_max = nums[0]
        local_min = global_min = float('inf')
        for n in nums[1:]:
            local_max = max(n+local_max, n)
            local_min = min(n+local_min, n)
            global_max = max(global_max, local_max)
            global_min = min(global_min, local_min)
        return max(global_max, sum(nums) if len(nums) <= 2 else sum(nums)-global_min)
