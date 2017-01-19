"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        i = 0
        isValid = True
        while i < len(s) and isValid:
            if s[i] in '([{':
                stack += s[i],
            elif stack:
                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    isValid = False
            else:
                isValid = False
            i += 1
        if stack: isValid = False
        return isValid
