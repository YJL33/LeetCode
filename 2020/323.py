"""
323
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        who = [i for _ in range(n)]

        def getRoot(x):
            while who[x] != x:
                x = who[x]
            return x

        for e in edges:
            a, b = min(e), max(e)
            rt_a, rt_b = getRoot(a), getRoot(b)
            if rt_a != rt_b:
                who[rt_a] = min(rt_a, rt_b)
                who[rt_b] = min(rt_a, rt_b)
        
        return sum([i == who[i] for i in range(n)])
            