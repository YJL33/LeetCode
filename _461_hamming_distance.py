"""
 461. Hamming Distance

    Total Accepted: 5441
    Total Submissions: 7355
    Difficulty: Easy
    Contributors: Samuri

The Hamming distance between two integers is:
the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 <= x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ^   ^

The above arrows point to positions where the corresponding bits are different.
"""
class Solution(object):
    def hammingDistance0(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a, b, cnt = bin(x)[2:].zfill(31), bin(y)[2:].zfill(31), 0
        for i in range(31):
            if a[i] != b[i]: cnt += 1
        return cnt

    def hammingDistance(self, x, y):
        # shorter:
        return bin(x^y).count('1')