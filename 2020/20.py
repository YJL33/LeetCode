"""
see https://leetcode.com/problems/valid-parentheses/
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use stack
        stack = []
        for i in xrange(len(s)):
            if s[i] in "({[":
                stack += s[i],
            else:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if s[i] == ')' and tmp == '(':
                    continue
                elif s[i] == ']' and tmp == '[':
                    continue
                elif s[i] == '}' and tmp == '{':
                    continue
                else:
                    return False

        return len(stack) == 0
