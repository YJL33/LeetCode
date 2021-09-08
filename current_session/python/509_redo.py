class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1]                      # dp[i] = self.fib(i)
        if n < len(dp): return dp[n]    # 0 or 1, len(dp) needs to be bigger than n

        while len(dp) != n+1:
            dp.append(dp[-1]+dp[-2])
        
        return dp[-1]
        
print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
print(Solution().fib(5))