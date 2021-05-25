'''
509
'''
class Solution:
    def fib(self, n: int) -> int:
        # dp
        dp = [0,1]
        if n < len(dp):
            return dp[n]
        else:
            cnt = 2
            while cnt != n+1:
                dp, cnt = [dp[-1], sum(dp)], cnt+1
            return dp[-1]

print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))