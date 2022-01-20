from functools import lru_cache
from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # use DP (top-down)

        @lru_cache(None)
        def dp(r1, c1, r2, c2):
            # if out of bound or on thorn
            if (r1 >= N or r2 >= N or c1 >= N or c2 >= N or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')

            if (r1 == N-1 and c1 == N-1):
                return grid[r1][c1]

            picked_up = grid[r1][c1]
            if (r1 != r2 and c1 != c2): picked_up += grid[r2][c2]

            # choose the optimal next state
            s1 = dp(r1+1, c1, r2+1, c2)     # down, down
            s2 = dp(r1, c1+1, r2, c2+1)     # right, right
            s3 = dp(r1, c1+1, r2+1, c2)     # right, down
            s4 = dp(r1+1, c1, r2, c2+1)     # down, right
            best_next_state = max([s1, s2, s3, s4])
            picked_up += best_next_state

            return picked_up
        
        return max(0, dp(0, 0, 0, 0))