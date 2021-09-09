# use DP

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)

        dp = [[0]*(M+1) for _ in range(N+1)]    # dp[i][j] = ans of text1[:i] and text2[:j]

        # if text1[i] == text2[j]: dp[i][j] = dp[i-1][j-1] + 1
        for i in range(N):
            for j in range(M):
                if text1[i]==text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1   # length of lcs + 1, e.g. (abcd, ac) => (abcde, ace)
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[-1][-1]
        