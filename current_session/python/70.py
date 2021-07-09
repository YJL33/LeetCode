class Solution:
    def climbStairs(self, n: int) -> int:
        # dp
        if n <= 3: return n
        dp, cur = [2,3], 3
        while cur != n:
            # steps required for n = steps required for n-1 + steps required for n-2
            dp = [dp[1], sum(dp)]
            cur += 1
        return dp[-1]