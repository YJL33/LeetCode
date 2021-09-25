# recursive => not good because some numbers are calculated too many times
# dp (use a dictionary to store calculated values)
# space optimization: use only array which has len=3
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return n
        if n <= 2: return 1
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            dp[i%3] = dp[(i-1)%3]+dp[(i-2)%3]+dp[(i-3)%3]
            # print('dp:', dp)
        
        return dp[n%3]

print(Solution().tribonacci(4))
print(Solution().tribonacci(25))
