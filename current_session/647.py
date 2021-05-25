"""
https://leetcode.com/problems/palindromic-substrings/
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # naive approach
        # list all i, j and check all i, j
        # O(n^3)
        res = 0
        for j in range(len(s)+1):
            for i in range(j):
                if s[i:j] == s[i:j][::-1]:
                    res += 1
        return res