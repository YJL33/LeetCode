"""
179. Largest Number

    Total Accepted: 55873
    Total Submissions: 271362
    Difficulty: Medium

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        numstr = [str(n) for n in nums]
        numstr.sort(cmp = lambda x, y: cmp(x+y, y+x))
        return ''.join(num).lstrip('0') or '0'