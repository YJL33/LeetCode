class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        #
        # Return the minimum number of moves that you need to determine with certainty what the value of f is.
        #
        # use DP
        # define DP[m][k] is the number of consecutive floors that 
        # we can check with m moves and k eggs (with certainty)
        #
        # consider general case:
        # throw 1 egg can check 1 floor. 
        # if break: you can check dp[m-1][k-1] floors, 
        # if not break: you can check dp[m-1][k] floors.
        # dp[m][k] = 1 + dp[m-1][k] + dp[m-1][k-1]
        #
        # in the worst case, we use n steps to check n floors
        # keep increase m (starting from 1, at most n moves)
        # seek until we have dp[m][k] >= given n floors, return m

        dp = [[0]*(k+1) for _ in range(n+1)]
        for m in range(1, n+1):
            for j in range(1, k+1):
                dp[m][j] = dp[m-1][j-1]+dp[m-1][j]+1
            print('dp[m]', dp[m], 'm=', m)
            if dp[m][k] >= n: return m
        return
    
    # try to explain binominal solution
    def superEggDrop_binominal(self, eggs: int, floors:int) -> int:

        def binomial(n, r):
            if r>n: return 0
            r, ans = min(r, n-r), 1
            for i in range(n, n-r, -1): ans *= i  # numerator
            for i in range(2, r+1): ans //= i     # denominator
            return ans
        
        lo, hi  = 1, floors
        while lo <= hi:
            mid = (lo+hi)//2
            # maximum floors that can be covered using "mid" drops, with given eggs
            max_floors = 0
            for i in range(1, eggs+1):
                max_floors += binomial(mid,i)
                # if more floors can be covered, try a lower "mid"
                if max_floors >= floors: 
                    hi = mid-1
                    break
            # if max_floors do not cover all floors, try a higher "mid"
            if max_floors< floors:
                lo = mid+1

        return lo

print(Solution().superEggDrop(1,2))
print(Solution().superEggDrop(2,6))
print(Solution().superEggDrop(3,14))
print(Solution().superEggDrop(2,100))