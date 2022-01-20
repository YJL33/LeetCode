from functools import lru_cache
from typing import List
import bisect
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # use DP
        # sort by start time
        # memoization
        # dp[i] = the solution fo attending ith event
        # either join or not join
        # use lru cache
        # use binary search to find the next available event

        events.sort()
        st = [e[0] for e in events]
        bs = {e: bisect.bisect_right(st, e) for _,e,_ in events}

        @lru_cache
        def dp(start, remaining=k):
            if start == len(events): return 0
            if remaining == 0: return 0
            s, e, v = events[start]
            j = bs[e]
            return max(dp(start+1, remaining), v+dp(j, remaining-1))
        
        return dp(0, k)

