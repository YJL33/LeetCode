"""
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic s in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp[i][j] = True if palindrome
        dp = self.initialize(len(s))
        maxLen, start, end = 0, 0, 0
        for i in xrange(len(s), -1, -1):
            for j in xrange(i, len(s)):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and (j-i) > maxLen:
                    maxLen, start, end = j-i, i, j
        return s[start:end+1]

    def initialize(self, length):
        dp = [[-1] * (length+1) for _ in xrange(length+1)]
        for i in xrange(length-1):
            dp[i][i+1] = True
        return dp

print Solution().longestPalindrome("abcda"), "a"
print Solution().longestPalindrome("abccba"), "abccba"
print Solution().longestPalindrome("aaaaaaaaaaa"), "aaaaaaaaaaa"
print Solution().longestPalindrome("abba"), "abba"
print Solution().longestPalindrome("ac"), "a"
print Solution().longestPalindrome(""), ""