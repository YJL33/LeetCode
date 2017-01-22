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
        # O(nlogn) solution
        size = len(nums)
        dp = []
        for x in xrange(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                #print "if", nums[x]
                dp.append(nums[x])
            else:
                #print "else", nums[x]
                dp[low] = nums[x]
            #print low, dp
        #print dp
        return len(dp)