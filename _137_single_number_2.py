"""
137 Single Number II
Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Dictionaries in python:
https://goo.gl/2vWop5
"""
class Solution(object):
    def singleNumber(self, nums):
        numberlist = {}
        for i in range(len(nums)):
            if nums[i] not in numberlist:
                numberlist[nums[i]] = 1
            else:
                numberlist[nums[i]] += 1
        for word in numberlist:
            if numberlist[word] == 1:
                return word