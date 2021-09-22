# use dfs+dict
# add all points into dict
# for each point, if not visited (new group),
# keep search and add all coline points into this group
# time analysis: O(n)

import collections
from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xd = collections.defaultdict(list) 
        yd = collections.defaultdict(list)

        for i in range(len(stones)):
            x, y = stones[i]
            xd[x].append(i)
            yd[y].append(i)

        visited = set()
        cntOfGroup = 0

        def dfs(i):
            visited.add(i)
            x, y = stones[i]
            for j in xd[x]:
                if j not in visited:
                    dfs(j)
            for k in yd[y]:
                if k not in visited:
                    dfs(k)
            return

        for i in range(len(stones)):
            if i not in visited:
                cntOfGroup += 1
                dfs(i)

        return len(stones)-cntOfGroup
