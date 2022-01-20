class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # use DP
        # DP[m][k] is the possible floor that u can check with m moves and k eggs
        # consider general case:
        # throw 1 egg can check 1 floor. 
        # if break: you can check dp[m-1][k-1] floors, 
        # if not break: you can check dp[m-1][k] floors.
        # dp[m][k] = 1 + dp[m-1][k] + dp[m-1][k-1]

        # at most n moves
        dp = [[0]*(k+1) for _ in range(n+1)]
        for m in range(1, n+1):
            for j in range(1, k+1):
                dp[m][j] = dp[m-1][j-1]+dp[m-1][j]+1
            if dp[m][k] >= n: return m
        
        return
    
    # try binominal solution
