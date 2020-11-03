"""
see https://leetcode.com/problems/generate-parentheses/
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n+1)]   # dp[i]: output of i as n
        dp[0] += '',
        for i in range(n+1):
            for j in range(i):
                # add some inside, and add the others outside
                dp[i] += ['('+x+')'+y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]

print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))