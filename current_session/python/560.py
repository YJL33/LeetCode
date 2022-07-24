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
from typing import List
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # clarification
        # any restrictions on time/space?
        # upper/lower bound of nums[i]?
        # upper/lower bound of k?
        
        # naive approach
        # try all i, j and check sum(nums[i:j+1])
        # time analysis: O(n^2) * O(n)
        
        # use prefix sum
        # for each n, add it into prefix sum, (say x) and check whether x-k is in prefix sum array or not
        # if so, add number of the occurance
        # use dictionary for to count seen prefix sum
        # key: prefix sum, value: count of prefix sum
        # time analysis: O(N) to go through the array, O(1) to query/add the key value pair to dict, worst case O(N) for serious hash collision
        # space analysis: O(N) to store both prefix-sum and prefix-sum count
        
        # test cases / optimization
        prefix_sum = 0
        seen, cnt = collections.Counter([0]), 0
        for n in nums:
            prefix_sum += n
            if prefix_sum-k in seen:
                cnt += seen[prefix_sum-k]
            seen[prefix_sum] += 1
        return cnt
            


    def subarraySum_dp(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # brute force - time O(n2)
        # dp - also time O(n2)
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        res = 0

        for i in range(len(nums)):
            for j in range(i+1):
                dp[j][i] = nums[i] + dp[j][i-1]
                if dp[j][i] == k:
                    res += 1

        # print dp
        return res

print(Solution().subarraySum([1,2,3], 3))
print(Solution().subarraySum([5,7,9,11,13,3], 16))
print(Solution().subarraySum([1], 1))
