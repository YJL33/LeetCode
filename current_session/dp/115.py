class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # use DP
        # dp[i][j] is the solution of s[:i] and t[:j]
        # (comparing s[:i] and t[:j])
        if s == t: return 1
        if any([c not in set(s) for c in t]): return 0

        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        # initial state
        for i in range(1,len(s)+1):
            dp[i][1] = dp[i-1][1]+1 if s[i-1] == t[0] else dp[i-1][1]
        
        # print('dp:', [dp[i][1] for i in range(len(s))])
        print('dp:', dp)
        for j in range(2,len(t)+1):
            for i in range(1,len(s)+1):
                if t[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

print(Solution().numDistinct("bbb", "b"))
print(Solution().numDistinct("rabbbit", "rabbit"))
print(Solution().numDistinct("babgbag", "bag"))