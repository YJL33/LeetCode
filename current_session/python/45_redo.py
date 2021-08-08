
from typing import List

# DP(?)
# dp[x] = solution of A[x]
#       = min(dp(for i in reachable_indexes)) + 1
# time complexity: O(n*w), w=avg step of each point
class Solution:
    def jumpDP(self, A: List[int]) -> int:
        dp = [float('inf') for _ in A]
        dp[0] = 0
        for i in range(len(A)):
            a = A[i]
            # for x in (i+1,i+a+1):
            x = i+1
            while x < min(len(A),i+a+1):
                dp[x] = min(dp[x], dp[i]+1)
                x += 1
        return dp[-1]

    # BFS O(n)
    def jump(self, A):
        farReach, end = 0, 0
        jp = 0
        for cur in range(len(A)-1):
            farReach = max(cur+A[cur], farReach)
            if cur == end:
                jp += 1
                end = farReach
                
        return jp