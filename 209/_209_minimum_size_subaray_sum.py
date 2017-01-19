"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

More practice:
If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log n).
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0                           # beginning of subarray
        sum_of_num = 0
        min_len = len(nums)+1
        for i in xrange(1, len(nums)+1):
            sum_of_num += nums[i-1]
            while sum_of_num >= s:          # nums[start] to nums[i-1]
                min_len = min(min_len, i-start)
                sum_of_num -= nums[start]   # Just minus the beginning element
                start += 1
        if min_len > len(nums): return 0
        return min_len
