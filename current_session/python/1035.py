from typing import List
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # 2d dp
        # dp[i][j] is the solution of A[:i] and B[:j]

        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        # maxSeen = 0

        for br in range(1, len(B)+1):
            for ar in range(1, len(A)+1):
                # compare B[:br] and A[:ar]
                if A[ar-1] == B[br-1]:
                    dp[ar][br] = dp[ar-1][br-1]+1
                else:
                    dp[ar][br] = max(dp[ar-1][br], dp[ar][br-1])
                # maxSeen = max(maxSeen, dp[ar][br])
        
        return dp[-1][-1]

print(Solution().maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
print(Solution().maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]))