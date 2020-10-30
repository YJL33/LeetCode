"""
see https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] in '()':
                if s[i] == '(':
                    stack += i,
                else:
                    if stack:
                        res += stack.pop(),
                        res += i,
            else:
                res += i,
        res.sort()
        return ''.join([s[i] for i in res])

print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
print(Solution().minRemoveToMakeValid("a)b(c)d"))
print(Solution().minRemoveToMakeValid("))(("))
print(Solution().minRemoveToMakeValid("(a(b(c)d)"))
