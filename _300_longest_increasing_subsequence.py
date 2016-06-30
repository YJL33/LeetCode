"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101],
therefore the length is 4. Note that there may be more than one LIS combination,
it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity? 
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n2) algorithm
        if not nums: return 0
        length = len(nums)
        res = [0 for i in xrange(len(nums))]
        for i in xrange(length):
            pre_prev = prev = float('-inf')
            temp = 0
            for j in xrange(i, length):
                if nums[j] > prev:
                    temp += 1
                    pre_prev = prev
                    prev = nums[j]
                elif pre_prev < nums[j] <= prev:
                    prev = nums[j]
            res[i] = temp
        return max(res)