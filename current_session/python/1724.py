from typing import List
import collections
class DistanceLimitedPathsExist:

    # use dfs (+union find for optimization)

    # initialization
    # craft adj-list
    # meanwhile, union those connected nodes with given undirected edges
    # pick one representative for each connected group

    # query
    # check if given p and q belong to same group or not
    # if so, then use dfs check the connectivity with given limit and adj list
    # (since union-find is crafted by p-to-root, q-to-root, we still need DFS)
    
    # time analysis: initialization
    #                O(E) to craft adj list
    #                O(E) to find representatives                               (optimization)
    #                O(N) for find/union, can use path compression into O(1)    (optimization)
    #                query
    #                O(logN) for dfs, worst scenario O(N)
    #                O(1) if they're not in the same group                      (optimization)
    # space analysis: O(N) for adj list, O(logN) for dfs visited nodes (and O(N) for representatives, optimization)
    
    def __init__(self, n: int, edgeList: List[List[int]]):
       
        self.who = [i for i in range(n)]                    # representative in union-find
        self.adj = collections.defaultdict(dict)
        
        # craft adj-list and union-find
        for a, b, w in edgeList:
            if b not in self.adj[a]:
                self.adj[a][b] = w
            else:
                self.adj[a][b] = min(self.adj[a][b], w)     # remove those duplicates
            if a not in self.adj[b]:
                self.adj[b][a] = w
            else:
                self.adj[b][a] = min(self.adj[b][a], w)
            
            # union
            a, b = self._get_root(a), self._get_root(b)
            if a != b:
                self.who[max(a,b)] = self.who[min(a,b)]
        # print('who', self.who)

    def query(self, p: int, q: int, limit: int) -> bool:
        if self._get_root(p) != self._get_root(q): return False
        return self._dfs(p, q, limit)
    
    def _get_root(self, x):
        if x == self.who[x]:
            return x
        self.who[x] = self._get_root(self.who[x])                  # path compression
        return self.who[x]
    
    def _dfs(self, start, target, limit):
        # do dfs with given limit
        st = [start]
        visited = set()
        while st:
            cur = st.pop()
            if cur == target:
                return True
            visited.add(cur)
            for nb, weight in self.adj[cur].items():
                if nb not in visited and weight < limit:
                    st.append(nb)
        return False

# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)