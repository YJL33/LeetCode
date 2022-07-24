class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        # use DP
        # first get longest common subsequence
        dp = [["" for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + s1[i]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key = len)
        lcs = dp[-1][-1]

        # add the 'uncommmon part' into supersequence
        res, i, j = "", 0, 0
        for c in lcs:
            while s1[i] != c:
                res += s1[i]
                i += 1
            while s2[j] != c:
                res += s2[j]
                j += 1
            res += c
            i, j = i+1, j+1

        # add the rest of strings
        return res+s1[i:]+s2[j:]