"""
44. Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        res = False
        star = -1
        for i in xrange(len(s)):
            if s[i] == p[i] or p[i] == '?':     # Match (single character), next
                continue
            elif p[i] == '*' and i < len(p):    # wildcard - sequence of character
                star = i                        # need to have a sequence of character in s
                j = star
                num_of_q = 0
                while p[j] == '*' or p[j] == '?' and j < len(p):   # p[j] = next non-wildcard char
                    j += 1
                    if p[j] == '?': num_of_q += 1       # Record the number of '?'
                # Now p[j] will be either next character or '*'






        return res
