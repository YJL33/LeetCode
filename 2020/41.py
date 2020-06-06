"""
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.

"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for example, the length of nums = 3
        # the 1st missing could only come from 1-4

        length = len(nums)

        res = {}
        for i in xrange(1, length+2):
            res[i] = 0

        for n in nums:
            if n in res:
                res[n] += 1

        for i in xrange(1, length+2):
            if res[i] == 0:
                return i

    def firstMissingPositive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # improvement: use array instead of dict

        length = len(nums)

        # res[i] = i
        res = [0 for _ in xrange(length+2)]

        for n in nums:
            if n > 0 and n <= length+1:
                res[n] += 1
                        
        for i in xrange(1, (length+2)):
            if res[i] == 0:
                return i