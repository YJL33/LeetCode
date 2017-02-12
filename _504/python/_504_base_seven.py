"""
504. Base 7

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Easy

Given an integer, return a base 7 representation of it as a String.

Example 1:

Input: 100
Output: "202"

Example 2:

Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""
class Solution(object):
    def convertTo7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res, pos = [], 1
        if num < 0:
            num, res = -num, ["-"]
        while pos*7 <= num:
            pos *= 7
        # now pos is the biggest position
        while pos != 0:
            res += str(num/pos),
            num = num%pos
            pos /= 7

        return ''.join(res)
