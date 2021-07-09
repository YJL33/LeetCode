"""
see https://leetcode.com/problems/generate-parentheses/
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        f(0): ""
        f(1): "("f(0)")"
        f(2): "("f(0)")"f(1), "("f(1)")"
        f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"
        So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"
        """
        dp = [[] for _ in range(n+1)]
        dp[0].append("")
        for i in range(1,n+1):
            for j in range(i):
            # t1 = ["(" + x + ")" + y for x in dp[-1] for y in ]
            # t2 = ["(" + x + ")" + y for ]
                dp[i] += ["(" + x + ")" + y for x in dp[i-j-1] for y in dp[j]]
        return dp[n]

print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))