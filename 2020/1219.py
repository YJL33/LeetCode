"""
1219
"""
from typing import List
class Solution:
    def getMaximumGold(self, A: List[List[int]]) -> int:

        h, w = len(A), len(A[0])
        
        def dfs(i, j, gold, path):
            # print('i, j, gold', i, j, gold ,path)
            gold += A[i][j]
            res = gold
            # print('collect:', A[i][j],'gold', gold)
            path.add((i,j))
            for a, b in (i+1, j), (i-1, j), (i,j+1), (i,j-1):
                if (a,b) not in path and 0 <= a < h and 0 <= b < w and A[a][b] != 0:
                    res = max(res, dfs(a, b, gold, set([x for x in path])))     # create a new path every dfs
                    # res = max(res, dfs(a, b, gold, path))
            return res
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    # print('start at:', i, j)
                    x = dfs(i,j,0,set())
                    ans = max(ans, x)
                    # print('=== current gold:', ans)
        return ans

# print(Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
# print(Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print(Solution().getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]))
