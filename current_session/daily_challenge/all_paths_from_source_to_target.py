from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # simple implement DFS
        # for each path, use a set to store visited nodes
        self.res = []
        def dfs(current, target, path, visited=set()):
            if current == target:
                self.res.append(path+[current])
                return

            visited.add(current)
            for nb in graph[current]:
                tmp = visited.copy()
                if nb not in visited:
                    dfs(nb, target, path+[current], tmp)
            return
        
        dfs(0, len(graph)-1, [])

        return self.res

print(Solution().allPathsSourceTarget([[1,2],[3],[3],[]]))
print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))