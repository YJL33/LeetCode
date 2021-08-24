from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # +/- 1 on each element
        # simply sort the element and pick the middle one
        # time complexity: O(nlogn)
        # does O(n) exist?
        nums.sort()
        m = len(nums)//2
        return sum([abs(nums[m]-n) for n in nums])

print(Solution().minMoves2([1,2,3]))
print(Solution().minMoves2([1,10,2,9]))