"""
 421. Maximum XOR of Two Numbers in an Array

    Total Accepted: 4822
    Total Submissions: 12133
    Difficulty: Medium
    Contributors: shen5630

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≦ ai < 2^31.

Find the maximum result of ai XOR aj, where 0 ≦ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force: find all pair and get max O(n^2)
        # build from left to right: O(n)
        # shift all number to right from 31 to 1 iteratively (say, snum)
        # suppose we know the prefix of answer (say, preans)
        # check whether preans^n exists in snums.
        # if exist: +1, else: +0
        preans = 0
        for i in range(32)[::-1]:
            preans <<= 1
            snums = {num >> i for num in nums}
            preans += any(preans^1^n in snums for n in snums)
        return preans