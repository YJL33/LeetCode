from typing import List
import collections
class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        # use DFS to check all the partitions(i,j)
        # store in DP[i][j] = max of A[i:j]
        if d > len(A): return -1
        if d == 1: return max(A)
        if d == len(A): return sum(A)

        dp = [[float('INF') for _ in range(len(A)+1)] for _ in range(len(A))]
        maxSeen = 0
        for i in range(len(A)):
            dp[i][i+1] = A[i]
            maxSeen = A[i]
            for start in range(i-1,-1,-1):
                maxSeen = max(maxSeen, A[start])
                dp[start][i+1] = maxSeen
        # print(dp)
        dfsMap = collections.defaultdict(int)

        def dfs(start, day):
            # we left A[start:]
            if (start, day) in dfsMap: return dfsMap[(start, day)]
            if day > len(A[start:]):
                return float('INF')
            if day == 1:
                return dp[start][-1]
            
            else:
                # print('given start:', start, 'day:', day)
                minSeen = float('INF')
                for j in range(start+1, len(A)):
                    minSeen = min(minSeen, dp[start][j] + dfs(j, day-1))
                    # print('minSeen:', minSeen)
                dfsMap[(start, day)] = minSeen
                return minSeen

        ans = dfs(0, d)
        return ans if ans != float('INF') else -1