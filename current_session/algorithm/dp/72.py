class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[0 for _ in range(len(w2)+1)] for _ in range(len(w1)+1)]

        for i in range(len(w1)+1):
            for j in range(len(w2)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

        return dp[-1][-1]