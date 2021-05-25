"""
161. One Edit Distance

    Total Accepted: 19345
    Total Submissions: 65045
    Difficulty: Medium
    Contributors: Admin

Given two strings S and T, determine if they are both one edit distance apart.
"""
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t: return False
        if len(s) < len(t): return self.isOneEditDistance(t, s)
        # now s must longer than t
        if len(s) - len(t) > 1: return False
        # check deletion/insertion distance
        elif len(s) - len(t) == 1:
            if len(t) == 0: return True
            i, j, diff = 0, 0, 0
            while j < len(t) and diff <= 1:
                if s[i] != t[j]: diff, i = diff+1, i+1
                else: i, j = i+1, j+1
            if j == len(t) and i == len(s)-1: diff += 1
        # check substitution distance
        else:
            assert len(s) == len(t)
            i, diff = 0, 0
            while i < len(s) and diff <= 1: 
                if s[i] != t[i]: diff += 1
                i += 1
        # return the result
        return True if diff == 1 else False