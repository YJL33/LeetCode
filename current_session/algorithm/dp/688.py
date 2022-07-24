import collections
from functools import lru_cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        # naive approach: recursion => TLE
        # dp top-down: memorize probability of each spot

        def inbound(x, y):
            return 0 <= x < n and 0 <= y < n

        @lru_cache
        def get_next_pos(r, c):
            res = []
            for a, b in [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]:
                if inbound(r+a, c+b):
                    res.append((r+a,c+b))
            return res
        
        res = 1
        pos = {(row, column):1}
        while k and res != 0:
            # print('k:', k)
            # print('pos:', pos, 'p:', res)
            t1, t2 = 0, 0
            layer = collections.defaultdict(int)          # pos: count
            for key, val in pos.items():
                r, c = key[0], key[1]
                next_pos = get_next_pos(r,c)
                for np in next_pos:
                    layer[np] += val
                t1 += len(next_pos)*val
                t2 += 8*val
            k -= 1
            pos = layer
            res *= t1/t2 if t2 else 0
        return res

print(Solution().knightProbability(8,30,6,4))
print(Solution().knightProbability(3,2,1,1))
