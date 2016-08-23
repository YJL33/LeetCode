"""
22. Generate Parentheses

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        temp = ''
        self.dfs(n, n, temp, res)
        return res

    def dfs(self, left, right, temp, res):
        if left == 0 and right == 0:
            res.append(temp)
        if left > 0:
            self.dfs(left-1, right, temp+'(', res)
        if right > left and right > 0:
            self.dfs(left, right-1, temp+')', res)