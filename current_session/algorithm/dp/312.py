from functools import lru_cache
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # use DP
        # dp[i][j] is the solution of nums[i:j+1]
        # answer = dp[0][len(nums)-1]
        # dp[i][j] = max(dp[i][k]+A[i]*A[k]*A[j]+dp[k][j]) for k in range(i+1, j)
        
        # be careful with the edge handling:
        # let's append 1 at the both end
        
        # try top-down
        
        A = [1]+nums+[1]
        L = len(A)
       
        @lru_cache(None)
        def dp(start, end):
            # print(start, end)
            if start+1 == end: return 0         # ignore this to make max part right for L==3
            return max(A[start]*A[k]*A[end] + dp(start,k) + dp(k,end) for k in range(start+1,end))
                
        return dp(0, L-1)
