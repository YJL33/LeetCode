"""
210
"""
from typing import List
import collections
class Solution:
    def findOrder(self, N: int, pre: List[List[int]]) -> List[int]:
        # make a prerequisite dict
        cd = collections.defaultdict(list)
        for a, b in pre:
            cd[a].append(b)
        # dfs
        self.visited = set()
        self.res = []
        self.loopFlag = False
        def dfs(x):
            self.visited.add(x)
            if x in cd:
                for p in cd[x]:
                    if p not in self.visited:
                        dfs(p)
                    elif p not in self.res:
                        self.loopFlag = True
            self.res.append(x)
            return
        
        for n in range(N):
            if n not in self.visited:
                dfs(n)
        return self.res if not self.loopFlag else []