"""
785
"""
# see https://leetcode.com/problems/is-graph-bipartite/discuss/115493/Python-7-lines-DFS-graph-coloring-w-graph-and-Explanation
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}                      # key, val: node - color

        def dfs(node):
            for n in graph[node]:
                if n not in color:
                    color[n] = -1*color[node]       # give the opposite color to nb
                    if not dfs(n):                  # ... and check the nb
                        return False
                else:                               # simply check whether it's opposite or not
                    if color[n] == color[node]:
                        # print('n, node', n, node)
                        return False
            return True

        for node in range(len(graph)):
            if node not in color:       # if not color yet, give one
                color[node] = 1
            if not dfs(node):           # check (and color) its neighbors
                return False
        return True

print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))
