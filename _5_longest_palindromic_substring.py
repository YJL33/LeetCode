"""
5. Longest Palindromic Substring

    Total Accepted: 131355
    Total Submissions: 550707
    Difficulty: Medium

Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length, longest = 0, ""
        for i in xrange(len(s)):
            #print i,
            r = l = i
            if r+(length/2) > len(s):
                break
            # check even
            if s[i] == s[i-1]:
                l -= 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    r, l = r+1, l-1
                #print s[l:r+1]
            # check odd
            r2 = l2 = i
            while l2 >= 0 and r2 < len(s) and s[l2] == s[r2]:
                r2, l2 = r2+1, l2-1
            #print s[l2:r2+1]
            if r2 > r:
                r, l = r2, l2
            if r-l+1 > length:
                length, longest = r-l+1, s[l+1:r]

        return longest
