from typing import List
import collections
class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        # its asking stones that can be grouped together
        # as long as they're vertically or horizontally co-line. e.g. shape as H, L, T, E ...
        # use dfs
        visited = set()

        yd = collections.defaultdict(list)
        xd = collections.defaultdict(list)

        for i in range(len(s)):
            x, y = s[i][0], s[i][1]
            yd[y].append(i)
            xd[x].append(i)

        def dfs(i):
            visited.add(i)
            for j in xd[s[i][0]]:
                if j not in visited:
                    dfs(j)
            for k in yd[s[i][1]]:
                if k not in visited:
                    dfs(k)
            return

        cnt = 0                     # count of co-line groups
        for i in range(len(s)):
            if i not in visited:
                cnt += 1
                dfs(i)
        
        return len(s)-cnt           # after removal, we have one point per group

print(Solution().removeStones([[0,0]]))
print(Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))