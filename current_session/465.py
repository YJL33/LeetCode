"""
465
"""
import collections
from typing import List
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # offset the depts
        bal = collections.defaultdict(int)
        for t in transactions:
            bal[t[0]] += t[2]
            bal[t[1]] -= t[2]
        
        D = [x for x in bal.values() if x != 0]    # debts

        def dfs(s):         # starting point
            while s<len(D) and D[s]==0:
                s += 1
            if s == len(D):
                return 0
            
            cnt = float('inf')
            for i in range(s+1, len(D)):
                if D[i]*D[s] < 0:
                    # settle i with s
                    D[i] += D[s]
                    cnt = min(cnt, 1+dfs(s+1))
                    # revert it
                    D[i] -= D[s]
            return cnt

        return dfs(0)


print(Solution().minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]]))
# [[6, 0, 50],[1, 6, 40],[2, 6, 10],[6, 3, 40],[6, 4, 10],[5, 6, 25]]
# [[0, 1, 10],[2, 0, 5]]
# [[0,1,5],[2,3,1],[2,0,1],[4,0,2]]
# [[0,1,5],[0,2,5],[3,4,5],[3,5,5]]