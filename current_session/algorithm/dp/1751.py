from functools import lru_cache
from typing import List
import bisect
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # use DP
        # sort by start time
        # memoization
        # dp(i) = the solution fo attending ith event

        events.sort()
        st = [e[0] for e in events]

        @lru_cache
        def dp(start, remaining=k):
            if start == len(events): return 0
            if remaining == 0: return 0
            _, e, v = events[start]
            j = bisect.bisect_right(st, e)
            return max(dp(start+1, remaining), v+dp(j, remaining-1))
        
        return dp(0, k)

    def maxValue_tablization(self, events: List[List[int]], k: int) -> int:        
        n = len(events)
        events.sort()
        starts = [e[0] for e in events]

        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            next_event = bisect.bisect_right(starts, events[i][1])
            for j in range(1, k+1):
                dp[i][j] = max(dp[i+1][j], events[i][2] + dp[next_event][j-1])
        
        return dp[0][k]