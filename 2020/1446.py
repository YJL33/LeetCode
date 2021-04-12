"""
1446
"""
from typing import List
import collections
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # use dfs and start from the root

        # build adjacency list
        ad = collections.defaultdict(list)      # road dict: key to val
        rd = collections.defaultdict(list)      # reversed dict
        for c in connections:
            ad[c[0]].append(c[1])
            rd[c[1]].append(c[0])

        # handle loop to check critical edges first
        # CORRECTION: No need to handle loop (since it is acyclic)

        # v1 = [False for _ in range(n)]
        # st = []
        # def dfs1(x):
        #     v1[x] = True
        #     for a in ad[x]:
        #         if not v1[a]:
        #             dfs1(a)
        #     st.append(x)
        
        # v2 = [False for _ in range(n)]
        # who = [-1 for _ in range(n)]
        # def dfs2(x, rep):
        #     v2[x] = True
        #     who[x] = rep
        #     for y in rd[x]:
        #         if not v2[y]:
        #             dfs2(y, rep)

        # for i in range(n):
        #     if not v1[i]:
        #         dfs1(i)
        # while st:
        #     x = st.pop()
        #     if not v2[x]:
        #         dfs2(x, x)
        
        # who array -> check representives
        # print(who)

        # visit reps only
        def dfs(x):
            visited[x] = True
            for a in ad[x]:
                if visited[a] != True:
                    # if who[a] != who[x]:
                    #     self.cnt += 1
                    self.cnt += 1
                    dfs(a)
            for b in rd[x]:
                if visited[b] != True:
                    dfs(b)
            return

        visited = [False for _ in range(n)]
        self.cnt = 0
        dfs(0)

        return self.cnt

print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
print(Solution().minReorder(5, [[0,1],[1,2],[2,3],[3,4]]))
print(Solution().minReorder(5, [[0,1],[1,2],[2,3],[3,4],[4,0]]))