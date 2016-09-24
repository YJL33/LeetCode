"""
44. Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # implement dp
        # dp[i][j] = True if s[:i] == p[:j]

        if len(s) < len(p)-p.count('*'):        # s is way too long
            return False

        m, n = len(s), len(p)
        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]
        dp[0][0] = True

        for i in xrange(m+1):
            for j in xrange(1, n+1):
                if p[j-1] not in '?*':
                    dp[i][j] = i > 0 and dp[i-1][j-1] and s[i-1] == p[j-1]
                elif p[j-1] == '?':
                    dp[i][j] = i > 0 and dp[i-1][j-1]
                else:
                    # star can act as 0, 1, or more than 1
                    dp[i][j] = (i > 0 and dp[i-1][j]) or dp[i][j-1]  # act as 0, 1

        #print dp
        return dp[-1][-1]
