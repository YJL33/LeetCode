from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # first, check how many 1s there
        N, L = sum(nums), len(nums)
        if N == L: return 0
        # use sliding window
        l, r = 0, N
        count = sum(nums[l:r])
        best_seen = N-count
        for _ in range(1,len(nums)):
            count -= nums[l]
            count += nums[r]
            best_seen = min(best_seen, N-count)
            l, r = l+1, (r+1)%L
        return best_seen

