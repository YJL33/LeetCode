"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/
"""
class Solution(object):
    def countSquares_TLE(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = []

        while matrix:
            ans += sum([sum(r) for r in matrix]),
            matrix = self.helper(matrix)

        return sum(ans)


    def helper(self, mat):
        m2 = [[0 for _ in range(len(mat[0])-1)] for _ in range(len(mat)-1)]

        for i in range(len(mat)-1):
            for j in range(len(mat[0])-1):
                sq = mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]
                m2[i][j] = 1 if sq == 4 else 0

        return m2

    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = matrix
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] *= min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

        return sum(map(sum, dp))

print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
print(Solution().countSquares([[1,0,1],[1,1,0],[1,1,0]]))