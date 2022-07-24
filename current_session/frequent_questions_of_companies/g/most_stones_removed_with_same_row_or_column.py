from typing import List
import collections
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # graph
        # coline-points are same group
        # largest number of stones can be removes = number of stones - number of groups
        
        # craft adj list
        # craft coline group

        adj_i = collections.defaultdict(list)      # key: i, val: list of ndex of stone
        adj_j = collections.defaultdict(list)
        for k in range(len(stones)):
            i, j = stones[k]
            adj_i[i].append(k)
            adj_j[j].append(k)
        
        who = [i for i in range(len(stones))]
        seen = set()

        def dfs(origin, root):
            if origin in seen: return
            seen.add(origin)
            who[origin] = who[root]
            i, j = stones[origin]
            for p in adj_i[i] + adj_j[j]:
                dfs(p, root)
            return

        for k in range(len(stones)):
            dfs(k, k)
        # print('who', who)

        return len(stones)-sum([who[i]==i for i in range(len(who))])

print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(Solution().removeStones([[0,0]]))