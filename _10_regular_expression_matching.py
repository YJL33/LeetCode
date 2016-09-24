"""
10. Regular Expression Matching

    Total Accepted: 98182
    Total Submissions: 428533
    Difficulty: Hard

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Implement DP
        # Define P[i][j] = True if s[:i] == p[:j]
        m, n = len(s), len(p)
        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]    # carefully arrange size
        dp[0][0] = True
        #print "inputs: ", s, p, dp
        for i in xrange(m+1):           # including m & n
            for j in xrange(1, n+1):    # arrange j in inner loop => increase p's index one by one
                #print "Now at:", i, j, s[:i], p[:j],
                if p[j-1] == '*':       # latest element
                    dp[i][j] = dp[i][j-2] or (i>0 and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                else:
                    dp[i][j] = i > 0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                #print dp[i][j], dp
        
        return dp[-1][-1]