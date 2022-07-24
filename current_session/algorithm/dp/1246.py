from typing import List
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        # use bottom-up DP
        # dp[i][j] is the solution of arr[i:j+1]
        
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        for l in range(len(arr)-1, -1, -1):
            for r in range(l, len(arr)):
                if l == r:
                    dp[l][r] = 1                # base case
                elif l+1 == r:
                    dp[l][r] = 1 if arr[l] == arr[r] else 2
                else:
                    # can reduce one in between even dp[l+1][r-1] is not palindrome
                    if arr[l] == arr[r]:
                        dp[l][r] = dp[l+1][r-1]
                    else:
                        dp[l][r] = dp[l+1][r-1]+2
                    
                    # need to check all possibilities in between
                    # e.g. [1,2,1,1,3,1] => should be 2
                    for m in range(l, r):
                        dp[l][r] = min(dp[l][r], dp[l][m]+dp[m+1][r])
        
            # print('dp', l, dp[l])
        return dp[0][-1]

print(Solution().minimumMoves([1,2,1,4,5,4,1,3,1]), '== 3')
print(Solution().minimumMoves([1,4,1,1,2,3,2,1]), "== 2")