"""
32. Longest Valid Parentheses

    Total Accepted: 73747
    Total Submissions: 323210
    Difficulty: Hard

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()",
    which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()",
which has length = 4.
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use dp: dp[i] = longest parentheses from pos 0 to i
        # 1. only update max length when r/l counteracts each other
        # 2. when appending new '(' into stack, if there's two () just merged,
        #   since this '(' will be connected with merged pairs
        #   modify the new element's index into earlier one.
        if not s:
            return 0

        dp = [0]*len(s)
        i, stack, lindex = 0, [], None      # stack only record lefts

        while i < len(s):
            if s[i] == '(':
                if lindex != None:
                    #print "use left index: ", lindex
                    stack.append(lindex)
                    lindex = None
                else:
                    stack.append(i)
                dp[i] = dp[i-1]
            elif s[i] == ')' and stack:     # here's a valid one
                left = stack.pop()
                lindex, length = left, i-left+1
                dp[i] = max(length, dp[i-1])
                #print "new pair: ", left, i
            else:
                lindex = None
                dp[i] = dp[i-1]
            i += 1

        #print dp
        return dp[-1]