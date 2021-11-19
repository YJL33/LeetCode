class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # first we want to know the 'union' of both str
        # use 2d-DP
        # dp[i][j] = min sum possible to achieve equal sum for s1[:i] and s2[:j]

        dp = [[float('inf') for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = 0

        for i in range(1,len(s1)):
            dp[i][0] = dp[i-1][0]+ord(s1[i-1])
        for j in range(1,len(s2)):
            dp[0][j] = dp[0][j-1]+ord(s2[j-1])

        for e2 in range(1, len(s2)+1):
            for e1 in range(1, len(s1)+1):
                # no need to delete anything
                if s1[e1-1] == s2[e2-1]:
                    # print('same')
                    dp[e1][e2] = dp[e1-1][e2-1]
                # which one we shoule remove here?
                # we should store the tmp string
                else:
                    dp[e1][e2] = min(
                        dp[e1-1][e2-1]+ord(s1[e1-1])+ord(s2[e2-1]),
                        dp[e1-1][e2]+ord(s1[e1-1]),
                        dp[e1][e2-1]+ord(s2[e2-1]))
                # print('wat now:', s1[:e1], s2[:e2], dp[e1][e2])
        # print('dp:', dp)
        return dp[-1][-1]

# print(Solution().minimumDeleteSum("tea", "tel"))
print(Solution().minimumDeleteSum("sea", "eat"))
print(Solution().minimumDeleteSum("delete", "leet"))