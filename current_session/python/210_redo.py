"""
210
"""
from typing import List
import collections
class Solution:
    def findOrder(self, N: int, pre: List[List[int]]) -> List[int]:
        self.loopFlag = False
        cd = collections.defaultdict(list)
        for a, b in pre:
            cd[a] += b,
        
        res = []
        visited = set()
        # dfs
        def dfs(i, res):
            visited.add(i)
            if i in cd:
                for p in cd[i]:
                    if p not in visited:
                        dfs(p, res)
                    elif p not in res:
                        self.loopFlag = True
            res += i,
            return

        for n in range(N):
            if n not in visited:
                dfs(n, res)
        
        return res if not self.loopFlag else []


print(Solution().findOrder(N = 2, pre = [[1,0]]))
print(Solution().findOrder(N = 4, pre = [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(N = 2, pre = [[1,0]]))
