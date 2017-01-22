"""
53. Maximum Subarray

Find the contiguous subarray within an array (having at least one number) that has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        curSum = maxSum = nums[0]
        for n in nums[1:]:                  # For each element n
            curSum = max(n, curSum + n)     # the maximum sum includes n
            maxSum = max(maxSum, curSum)    # the maximum sum (no matter including n or not)

        return maxSum
