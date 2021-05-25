"""
1. Two Sum

Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Accepted 2.9M
Submissions 6.5M
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force: time O(n^2)
        # memorize seen numbers: time O(n), space O(n)

        numsDict = {}           # key: number, value: index
        
        for i in xrange(len(nums)):
            counterPart = target - nums[i]
            if counterPart in numsDict:
                return [numsDict[counterPart], i]
            numsDict[nums[i]] = i

        return

print Solution().twoSum([4, 6, 7, 11, 5], 12)
