class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        # 2D DP
        # dp[i+1][j+1] = solution of a[:i+1] and b[:j+1]

        dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

        for br in range(1,len(b)+1):
            for ar in range(1, len(a)+1):
                if b[br-1] == a[ar-1]:
                    dp[ar][br] = dp[ar-1][br-1]+1
                else:
                    dp[ar][br] = max(dp[ar][br-1], dp[ar-1][br])
        
        return dp[-1][-1]

