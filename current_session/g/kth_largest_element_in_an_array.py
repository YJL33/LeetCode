from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        # use heap: each operation cost logN, time Complexity: O(NlogN)
        # sort: time Complexity: O(NlogN)
        nums.sort()
        return nums[~(k-1)]

print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))