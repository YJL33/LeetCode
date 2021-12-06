from typing import List
from collections import defaultdict
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # find the euler trail
        # by the question, the trail must exist
        # see more at 
        # https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/tu-xing-yan-suan-fa-euler-circuit

        deg = defaultdict(int)
        adj = defaultdict(list)
        for u, v in pairs:
            adj[u].append(v)
            deg[u] += 1
            deg[v] -= 1
        _, src = max((v, k) for k, v in deg.items())
        ans = []
        def _f(u):
            # ans.append(u)
            while adj[u]:
                # v = adj[u].pop(0)
                v = adj[u].pop()
                _f(v)
            ans.append(u)
        _f(src)
        n = len(ans)
        # print('ans:', ans)
        # return [[ans[i], ans[i+1]] for i in range(n-1)]
        return [[ans[n-i-1], ans[n-i-2]] for i in range(n-1)]

print(Solution().validArrangement([[5,1],[4,5],[11,9],[9,4]]))
print(Solution().validArrangement([[1,3],[3,2],[2,1]]))
print(Solution().validArrangement([[1,2],[1,3],[2,1]]))
# print(Solution().validArrangement([[874,518],[649,247],[621,559],[774,166],[241,168],[835,421],[168,835],[835,399],[741,436],[958,526],[166,578],[734,812],[436,297],[813,774],[166,559],[518,548],[882,719],[559,741],[819,621],[720,168],[964,187],[518,781],[166,781],[781,436],[719,958],[342,241],[659,392],[27,513],[812,468],[513,910],[187,848],[510,741],[835,392],[813,559],[392,848],[964,813],[241,958],[958,436],[854,241],[813,719],[781,421],[421,649],[720,910],[510,297],[725,835],[848,271],[483,578],[848,336],[854,592],[559,720],[436,399],[297,958],[592,483],[526,734],[854,813],[40,720],[719,510],[548,964],[910,882],[342,854],[578,518],[399,514],[514,813],[22,854],[399,342],[336,297],[392,271],[813,835],[27,166],[436,725],[271,854],[468,659],[421,166],[168,548],[297,526],[271,964],[741,725],[548,27],[910,510],[559,27],[73,40],[526,510],[247,819],[725,874],[578,342],[297,22],[510,813]]))
