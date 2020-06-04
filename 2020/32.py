"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Accepted 275.1K
Submissions 985.6K
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return 0

        res = 0

        stack, lastLeft = [], None

        for i in xrange(len(s)):
            # print "i: ", i, lastLeft
            if s[i] == '(':
                if lastLeft != None:
                    stack.append(lastLeft)
                    lastLeft = None
                else:
                    stack.append(i)
            else:                               # s[i] == ')'
                if stack:
                    lastLeft = stack.pop()
                    res = max(res, i-lastLeft+1)
                else:
                    lastLeft = None

        return res

print Solution().longestValidParentheses(")()())()()(")
