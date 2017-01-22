"""
172. Factorial Trailing Zeroes

    Total Accepted: 71915
    Total Submissions: 210550
    Difficulty: Easy

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while (n//5):
            res, n = res+(n//5), (n//5)

        return res
