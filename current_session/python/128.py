"""
128

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x-1 not in nums:             # start from smallest
                y = x+1
                while y in nums: y += 1     # find the length of consecutive
                best = max(best, y-x)
        return best
