"""
560. Subarray Sum Equals K

Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Accepted 299.4K
Submissions 683.3K
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # use hashmap - time O(n)
        seenSum = {}
        seenSum[0], subSum, count = 1, 0, 0

        for n in nums:
            subSum += n
            if subSum-k in seenSum:
                count += seenSum[subSum-k]
            if subSum in seenSum:
                seenSum[subSum] += 1
            else:
                seenSum[subSum] = 1

        return count



    def subarraySumDP(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # brute force - time O(n2)
        # dp - also time O(n2)
        dp = [[0 for _ in xrange(len(nums))] for _ in xrange(len(nums))]
        res = 0

        for i in xrange(len(nums)):
            for j in xrange(i+1):
                dp[j][i] = nums[i] + dp[j][i-1]
                if dp[j][i] == k:
                    res += 1

        # print dp
        return res

print Solution().subarraySum([1,2,3], 3)
print Solution().subarraySum([5,7,9,11,13,3], 16)
print Solution().subarraySum([1], 1)
