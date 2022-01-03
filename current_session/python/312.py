from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # use DP
        # dp[i][j] is the solution of nums[i:j+1]
        # answer = dp[0][len(nums)-1]

        A = [1]+nums+[1]
        L = len(A)
        dp = [[0]*L for _ in range(L)]

        for i in range(L-2, -1, -1):
            for j in range(i+2, L):
                dp[i][j] = max(A[i]*A[k]*A[j] + dp[i][k] + dp[k][j] for k in range(i+1, j))
        
        return dp[0][L-1]

