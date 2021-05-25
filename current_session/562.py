"""
see https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
"""
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # use DP
        # for m in M: print(m)
        if not M: return 0

        # horizontal, vertical, diag, anti-diag
        dp, maxSeen = [[[0,0,0,0] for _ in m]for m in M], 0

        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]:                 # check h, v, d, a
                    dp[i][j] = [1,1,1,1]
                    if j-1>=0 and M[i][j-1]:
                        dp[i][j][0] += dp[i][j-1][0]
                    if i-1>=0 and M[i-1][j]:
                        dp[i][j][1] += dp[i-1][j][1]
                    if i-1>=0 and j-1>=0 and M[i-1][j-1]:
                        dp[i][j][2] += dp[i-1][j-1][2]
                    if i-1>=0 and j+1<len(M[0]) and M[i-1][j+1]:
                        dp[i][j][3] += dp[i-1][j+1][3]
                    maxSeen = max([maxSeen]+dp[i][j])

        return maxSeen

print(Solution().longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))
print(Solution().longestLine([[0,1,1,0],[0,1,1,0],[1,0,0,0],[1,1,1,1]]))
