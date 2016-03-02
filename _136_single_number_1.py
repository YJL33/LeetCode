"""
Implement:
Exclusive Or: https://en.wikipedia.org/wiki/Exclusive_or
"""
class Solution(object):
    def singleNumber(self, nums):
        k = 0
        for i in nums:
            k ^= i
        return k