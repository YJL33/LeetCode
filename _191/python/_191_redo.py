"""
 191. Number of 1 Bits

    Total Accepted: 134151
    Total Submissions: 346914
    Difficulty: Easy
    Contributors: Admin

Write a function that takes an unsigned integer and returns the number of ''1' bits it has
(also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
so the function should return 3.
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            cnt, n = cnt+(n&1), n>>1
        return cnt
