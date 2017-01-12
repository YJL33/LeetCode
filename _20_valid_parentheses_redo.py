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
        stack, i, left, right = [], 0, '([{', ')]}'

        for c in s:
            if c in left: stack += c,
            elif stack and right.index(c) == left.index(stack[-1]): stack.pop()
            else: return False

        return len(stack) == 0
