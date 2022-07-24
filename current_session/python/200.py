"""
see https://leetcode.com/problems/number-of-islands/
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # clarification:
        # any restriction on time/space? (e.g. timeout, memory)
        # is the grid always valid? (e.g. "2"?)
        # upperbound/lowerbound of H and W?
        # may I modify the given grid?
        
        # union-find approach
        # 2-pass
        # 1st pass, label all seen land. 
        # 2nd pass, if 2 pixels are connected, link them together (union-find)
        # since all labels are now unioned, count the number of representatives (groups)
        # e.g. after 1st pass: we have label [0,1,2,3,4,5,6,7] => none of them are connected, therefore we have 8 islands
        # e.g. after 1st pass: we have label [0,1,2,3,4,5,6,7] => after union [0,1,1,1,1,5,5,5] => therefore we have 3 islands
        # time analysis:
        # scan whole grid: O(HW) to label
        # union-find: O(A)*O(logL), where A is the area of land, and for each land we need to find its root (representative),
        # avg case O(logL) where L is the number of all labels, worst cast O(L), with path compression O(1) (update its root while finding)
        # space analysis: O(HW) if not allowed to modify, O(L) where L is the number of all labels
        
        # DFS approach
        # scan the whole grid, if see any island, count 1 and mark all the connected pixels as '0'
        # time analysis: O(HW) to scan the whole grid, O(A) where A is the area of islands, worst case O(HW) (in worst case each grid point will be visited twice)
        # space analysis: O(HW) if not allowed to modify, O(depth) for the depth of of recursive calls => implement iteratively to improve
        
        H, W = len(grid), len(grid[0])
        cnt = 0
        
        def dfs(r,c):
            st = [(r,c)]
            while st:
                i, j = st.pop()
                grid[i][j] = "0"
                for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=a<H and 0<=b<W and grid[a][b] == "1":
                        st.append((a,b))
            return
        
        for i in range(H):
            for j in range(W):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        
        return cnt

    def numIslands_uf(self, grid: List[List[str]]) -> int:
        H, W = len(grid), len(grid[0])
        new_grid = [[-1 for _ in range(W)] for _ in range(H)]
        l = 0

        # 1st pass: labeling
        for i in range(H):
            for j in range(W):
                if grid[i][j] == "1":
                    new_grid[i][j], l = l, l+1

        # initialization
        labels = [i for i in range(l)]

        # 2nd pass: union-find
        def find(x):
            if x == labels[x]:
                return x
            labels[x] = find(labels[x])         # path compression
            return labels[x]

        def union(i1, j1, i2, j2):
            root1, root2 = find(new_grid[i1][j1]), find(new_grid[i2][j2])
            if root1 != root2:
                labels[max(root1, root2)] = min(root1, root2)
            return

        for i in range(H):
            for j in range(W):
                if new_grid[i][j] != -1:            # we have a node here, check if there's an edge
                    if i-1 >= 0 and new_grid[i-1][j] != -1:
                        union(i, j, i-1, j)
                    if j-1 >= 0 and new_grid[i][j-1] != -1:
                        union(i, j, i, j-1)
        
        return sum([i == labels[i] for i in range(len(labels))])

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), "should be 1")
print(Solution().numIslands([["1","1","0","1","0"],["1","1","1","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), "should be 1")
print(Solution().numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]), "should be 1")
print(Solution().numIslands([["1","0","1","1","0","0","1","0","1","1","1","1","0","1","0","1","1","1","1","0"],["0","1","0","0","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1"],["1","0","0","1","0","1","0","1","0","1","1","0","1","1","1","0","0","1","1","0"],["0","1","1","0","0","1","1","0","1","1","1","1","0","0","1","0","0","0","1","1"],["1","1","0","1","0","0","1","0","0","0","1","0","1","0","1","1","1","0","1","1"],["0","0","0","0","1","0","1","1","0","0","1","0","0","1","0","1","1","1","1","0"],["1","0","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","0","1","0"],["0","1","1","0","0","0","1","0","0","1","0","1","1","1","0","0","1","1","0","1"],["0","0","0","0","1","1","0","1","0","0","1","1","0","1","0","0","1","0","1","0"],["0","0","1","1","1","0","1","0","1","0","1","1","1","0","1","1","1","1","1","0"],["1","0","1","0","1","1","1","0","1","1","1","0","1","0","1","0","1","0","1","1"],["0","0","1","1","1","1","0","1","1","1","0","1","0","0","0","1","1","1","0","1"],["1","1","1","0","0","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0"],["0","0","1","1","1","0","0","1","0","0","1","1","1","1","1","1","0","1","1","0"],["0","0","0","1","1","0","0","0","0","1","1","0","1","0","0","1","1","1","1","1"],["0","1","1","1","0","1","0","0","1","1","1","1","1","0","1","1","1","0","0","1"],["0","0","0","0","1","1","1","1","0","0","0","0","1","0","0","0","0","1","1","0"],["1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1"],["0","1","0","0","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1"],["0","0","1","1","1","1","1","0","0","0","1","1","1","1","1","1","0","1","1","0"]]), "should be 23")

print(Solution().numIslands_uf([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), "should be 1")
print(Solution().numIslands_uf([["1","1","0","1","0"],["1","1","1","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), "should be 1")
print(Solution().numIslands_uf([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]), "should be 1")
print(Solution().numIslands_uf([["1","0","1","1","0","0","1","0","1","1","1","1","0","1","0","1","1","1","1","0"],["0","1","0","0","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1"],["1","0","0","1","0","1","0","1","0","1","1","0","1","1","1","0","0","1","1","0"],["0","1","1","0","0","1","1","0","1","1","1","1","0","0","1","0","0","0","1","1"],["1","1","0","1","0","0","1","0","0","0","1","0","1","0","1","1","1","0","1","1"],["0","0","0","0","1","0","1","1","0","0","1","0","0","1","0","1","1","1","1","0"],["1","0","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","0","1","0"],["0","1","1","0","0","0","1","0","0","1","0","1","1","1","0","0","1","1","0","1"],["0","0","0","0","1","1","0","1","0","0","1","1","0","1","0","0","1","0","1","0"],["0","0","1","1","1","0","1","0","1","0","1","1","1","0","1","1","1","1","1","0"],["1","0","1","0","1","1","1","0","1","1","1","0","1","0","1","0","1","0","1","1"],["0","0","1","1","1","1","0","1","1","1","0","1","0","0","0","1","1","1","0","1"],["1","1","1","0","0","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0"],["0","0","1","1","1","0","0","1","0","0","1","1","1","1","1","1","0","1","1","0"],["0","0","0","1","1","0","0","0","0","1","1","0","1","0","0","1","1","1","1","1"],["0","1","1","1","0","1","0","0","1","1","1","1","1","0","1","1","1","0","0","1"],["0","0","0","0","1","1","1","1","0","0","0","0","1","0","0","0","0","1","1","0"],["1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1"],["0","1","0","0","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1"],["0","0","1","1","1","1","1","0","0","0","1","1","1","1","1","1","0","1","1","0"]]), "should be 23")