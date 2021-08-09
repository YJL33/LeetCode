class Solution:
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = matrix
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

        return sum(map(sum, dp))