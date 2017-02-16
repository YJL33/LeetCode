"""
 258. Add Digits

    Total Accepted: 148844
    Total Submissions: 295667
    Difficulty: Easy
    Contributors: Admin

Given a non-negative integer num,
repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return it.
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if (num%9):
            return num%9
        else:
            return 0 if (num == 0) else 9