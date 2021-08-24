# create a adjacnecy List
# use dfs to find target
from typing import List
import collections
class Solution:
    def calcEquation(self, eq: List[List[str]], val: List[float], queries: List[List[str]]) -> List[float]:
        numDict = collections.defaultdict()
        for i in range(len(eq)):
            a, b = eq[i]
            if a not in numDict: numDict[a] = collections.defaultdict(int)
            numDict[a][b] = val[i]
            if b not in numDict: numDict[b] = collections.defaultdict(int)
            numDict[b][a] = 1/val[i]
        
        # print('nd',numDict)
        res = []

        def dfs(p, q, visited):
            if p in visited:
                return
            if q in numDict[p]:
                return numDict[p][q]
            
            visited.add(p)
            for k, v in numDict[p].items():
                tmp = dfs(k, q, visited)
                if tmp:
                    return v*tmp
            visited.remove(p)
            return

        for j in range(len(queries)):
            p, q = queries[j]
            visited = set()
            if p not in numDict or q not in numDict:
                x = -1.0
            elif p == q:
                x = 1.0
            else:
                x = dfs(p, q, visited)
            res.append(x if x is not None else -1.0)
        
        return res

# print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
# print(Solution().calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
# print(Solution().calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))
print(Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],[3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
