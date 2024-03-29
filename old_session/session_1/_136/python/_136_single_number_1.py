"""
136 Single Number
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
Implement:
Exclusive Or: https://en.wikipedia.org/wiki/Exclusive_or
"""
class Solution(object):
    def singleNumber(self, nums):
        k = 0
        for i in nums:
            k ^= i
        return k