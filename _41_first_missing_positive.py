"""
41. First Missing Positive

    Total Accepted: 75693
    Total Submissions: 308437
    Difficulty: Hard

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # put everything into correct position (just ignore 0 and negatives)
        # suppose nums = [4,3,5,2,6,1]
        # correct position should be: [1,2,3,4,5,6]
        # Therefore, we can ignore n:   1. n <= 0   2. n > len(nums)    3. duplicates
        if not nums:
            return 1

        for i in xrange(len(nums)):
            # suppose n[5] = 1 => we want n[0] = 1 => swap with n[0]
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:      # valid
                nums[n-1], nums[i] = nums[i], nums[n-1]     # keep swap until no more opeartions

        for j in xrange(len(nums)):
            if nums[j] != j+1:
                return j+1

        return len(nums)+1