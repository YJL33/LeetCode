"""
see https://leetcode.com/problems/maximum-vacation-days/

n cities: (0 to n-1)
intial: city0, Monday
flights: flights[i][j] == 1 if there's a flight for city i to j (else no)
total k weeks
days: day[a][b] means max days u can take in city a in week b
"""
from typing import List
import collections
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        # use DP
        # iterate by week
        N, K = len(days), len(days[0])
        dp = [-1 for _ in range(N)]         # vacations that u can take
        dp[0] = 0                           # initial state

        # craft adj list
        flyDict = collections.defaultdict(list)
        for i in range(N):
            for j in range(N):
                if flights[i][j]:
                    flyDict[i].append(j)
        
        for w in range(K):
            tmp = [-1 for _ in range(N)]                    # solution at given day
            for city in range(N):
                if dp[city] >= 0:
                    tmp[city] = max(tmp[city], dp[city]+days[city][w])
                    for dest in flyDict[city]:
                        tmp[dest] = max(tmp[dest], dp[city]+days[dest][w])
            dp = tmp
        
        return max(dp)

print(Solution().maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]))
print(Solution().maxVacationDays([[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]))
print(Solution().maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]))
print(Solution().maxVacationDays([[0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0],[1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1],[1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0],[0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0],[0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1],[0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0],[0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1,1,1],[1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0],[0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1],[1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0],[0,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,0],[0,1,1,1,0,1,0,0,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0],[0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1],[0,1,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0],[0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1],[0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1],[1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0],[1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,1,0,1],[1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,1,0,0,1],[0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0],[1,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1],[1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0],[0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0],[1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1],[1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,0],[1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,1,0,1],[0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0],[0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,0,1,0],[1,0,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1],[1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1],[1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,1],[1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,1],[0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0],[0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1],[1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0],[0,0,1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1],[1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1],[0,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0],[1,1,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0],[1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1],[0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,1,0],[0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,0,1],[0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1],[0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1],[1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0],[0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,0,0],[1,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0],[1,0,1,0,0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1],[0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,1],[1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0],[0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0],[1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,1],[1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1],[1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0],[1,0,1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0],[1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0],[0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1],[1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0],[1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0],[1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,1,1,1,1],[1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0],[1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1],[0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0],[1,0,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,0,0,1,1,1,1,0,0,1],[0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1,1,0],[0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1],[0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1],[1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1],[1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0],[1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,0],[1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0],[0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,0],[1,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1],[0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0],[1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0],[0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0],[1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1],[0,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0],[1,1,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,0],[1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1],[0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,1],[0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1],[0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],[0,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1],[1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0],[1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1],[1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1],[0,0,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1],[1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,0],[1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1],[0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1],[1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1],[1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1],[0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0],[1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0]],[[0,2,1,0,0,1,0,0,2,0,2,0,1,0,2,1,1,1,1,0,2,0,1,1,2,1,0,2,0,2,0,2,2,1,0,2,2,0,0,1,2,1,1,0,1,0,1,2,1,1,2,2],[0,1,0,1,1,2,1,0,1,0,2,1,2,1,2,0,1,2,0,2,0,2,0,0,2,2,0,1,0,0,2,1,0,2,1,0,2,2,0,2,0,2,0,1,1,0,2,0,2,0,2,2],[0,0,1,1,0,1,1,0,0,1,2,1,2,0,2,2,0,1,0,1,2,1,0,0,2,2,2,0,2,1,2,1,2,1,2,0,0,2,0,1,0,1,1,2,2,2,2,0,0,0,0,1],[1,0,2,2,0,2,2,0,0,2,2,2,1,1,1,1,2,0,2,2,1,2,1,2,0,0,2,1,0,2,2,2,1,1,1,2,1,0,2,0,2,1,1,0,2,1,0,0,1,2,0,0],[2,0,1,0,1,0,2,1,2,2,2,2,0,0,0,1,2,2,1,2,1,0,0,0,2,1,0,2,1,2,0,1,1,0,1,1,1,2,2,1,0,2,2,2,1,0,0,0,1,2,1,2],[0,2,0,1,2,0,2,1,0,0,2,2,1,0,2,2,1,1,1,2,1,1,1,0,1,1,2,1,0,0,2,0,1,1,0,0,0,1,0,2,1,1,0,0,0,0,0,0,1,2,0,1],[0,2,1,1,1,2,0,0,0,0,2,1,1,1,0,2,2,2,2,0,0,0,1,0,2,0,0,1,0,0,2,0,2,0,2,2,2,2,2,0,1,0,2,2,0,1,2,2,2,1,2,0],[2,2,1,1,0,2,0,2,2,1,2,2,1,0,1,0,0,2,2,1,0,2,0,2,0,0,2,1,0,1,1,0,1,0,0,2,2,2,2,1,0,2,0,2,1,1,1,0,0,0,2,1],[1,0,0,1,2,0,0,0,0,0,0,1,1,1,0,2,2,2,2,2,2,1,1,2,2,2,0,1,1,2,2,1,2,0,0,0,2,2,0,1,1,2,2,0,2,2,2,2,0,2,1,0],[2,1,0,1,2,2,2,1,1,0,2,2,0,0,1,1,1,2,0,2,1,1,1,1,0,0,2,1,2,2,2,1,2,0,1,1,0,2,0,2,1,0,0,2,2,0,2,0,1,1,2,0],[0,1,0,1,0,1,1,0,2,2,0,2,2,1,2,2,1,2,1,0,0,0,1,1,1,2,0,0,1,2,0,0,0,1,0,1,2,1,2,1,1,2,2,0,1,2,2,0,0,1,0,2],[0,1,0,0,2,1,0,2,0,0,1,0,0,2,0,2,2,1,2,2,1,1,0,0,0,0,1,2,0,0,0,0,1,0,1,1,1,2,0,0,0,1,1,1,0,2,2,1,0,1,1,2],[1,0,1,0,2,0,2,1,2,1,0,0,0,1,2,2,1,0,1,0,0,2,2,2,0,1,0,0,1,1,1,1,0,2,0,1,1,0,1,0,1,2,0,2,1,2,1,0,1,0,2,2],[0,2,1,2,1,1,2,2,1,0,1,1,0,2,2,2,2,1,0,2,0,0,2,1,2,2,1,0,1,1,1,0,2,1,0,1,0,0,2,1,1,2,0,2,2,0,1,1,2,0,2,0],[2,2,2,2,0,2,2,1,1,2,1,2,1,1,2,1,2,2,1,2,0,2,2,2,1,0,2,2,0,0,1,1,0,0,0,1,2,1,1,1,1,2,0,1,1,1,1,2,1,0,2,0],[2,2,1,2,2,2,1,0,0,0,1,1,1,2,1,0,1,2,0,2,0,1,2,1,0,1,2,0,1,2,2,0,1,0,2,2,0,2,2,0,0,0,1,0,0,0,1,0,1,1,0,2],[1,0,0,1,2,0,0,1,0,2,2,2,2,1,0,1,0,2,0,0,2,2,0,0,2,1,1,2,2,2,1,1,1,1,0,2,1,2,2,2,1,0,2,0,2,0,1,0,0,1,1,0],[2,1,0,0,2,2,0,2,0,1,0,2,2,2,1,2,0,0,1,1,2,1,1,0,0,2,1,1,0,1,0,0,0,1,2,2,1,1,1,1,0,0,2,2,1,0,2,0,1,1,1,0],[2,0,1,0,1,0,2,2,0,1,2,2,0,1,1,1,0,1,1,1,1,1,2,2,2,2,0,0,2,2,2,2,2,1,0,0,1,1,0,0,0,2,2,1,0,1,1,1,0,1,2,0],[0,1,1,2,2,1,0,1,1,1,1,1,2,1,0,1,2,1,1,2,0,1,2,0,0,1,2,2,0,1,2,1,2,1,2,2,0,1,2,1,0,1,2,1,2,0,1,0,1,1,2,0],[1,0,1,2,2,1,1,0,1,2,2,2,0,0,2,1,1,0,1,0,2,2,1,2,2,0,1,1,0,1,2,1,0,2,0,1,2,2,1,2,2,2,2,1,1,1,1,0,2,0,2,1],[2,2,1,2,1,0,1,2,0,0,0,1,1,0,0,0,1,2,0,2,2,0,1,1,0,2,2,0,1,1,2,0,1,2,0,2,0,0,2,2,2,1,0,1,2,2,0,2,0,1,0,2],[1,2,2,0,0,0,1,0,1,0,2,2,2,1,1,2,0,0,1,2,2,2,1,0,2,1,0,2,2,2,2,0,0,0,1,2,1,2,0,0,1,0,2,1,2,2,1,1,0,1,1,0],[2,2,1,1,1,1,2,2,2,2,1,0,1,1,0,1,2,0,2,1,2,1,1,2,1,0,2,2,0,1,2,1,1,2,2,2,2,2,2,1,2,0,2,0,2,2,0,1,1,1,2,1],[0,2,2,2,2,1,1,0,2,1,1,2,2,2,0,1,2,1,0,2,0,1,2,1,0,0,1,0,1,1,2,0,1,0,1,0,1,2,0,0,0,1,0,2,2,2,1,1,1,0,0,2],[0,2,1,0,2,0,1,2,2,2,0,2,0,1,1,2,1,0,2,1,0,1,2,1,0,0,2,0,1,1,0,2,0,1,1,0,2,0,1,2,1,1,1,1,1,1,0,1,0,2,1,0],[2,2,1,1,2,0,1,2,2,1,2,0,1,2,0,1,2,0,2,0,0,2,2,2,2,1,2,0,2,0,1,2,0,2,1,2,1,1,1,1,1,0,1,0,0,2,0,2,1,2,1,1],[1,0,0,2,2,2,0,0,0,1,0,2,2,0,0,0,1,0,2,2,1,2,2,1,2,0,1,2,0,0,0,0,1,0,1,1,0,0,1,2,2,2,1,1,0,0,2,1,2,2,1,2],[1,1,0,2,2,1,2,2,2,1,0,0,2,1,0,2,2,0,0,2,0,0,1,0,2,1,2,0,0,0,2,2,2,0,1,2,1,0,2,0,0,2,1,1,2,1,1,1,1,0,1,1],[2,2,2,0,0,1,0,0,2,2,2,1,2,1,0,2,1,2,1,2,2,1,1,2,1,2,1,1,0,1,2,2,2,2,1,1,2,0,1,0,1,2,1,2,0,0,1,0,1,0,1,2],[2,0,2,0,0,1,1,0,1,1,1,2,1,2,0,0,1,0,1,1,1,1,0,0,2,2,0,1,2,2,0,2,2,2,1,0,2,2,2,2,1,2,1,1,2,0,2,0,2,1,0,2],[1,0,1,2,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,2,0,2,2,1,1,2,1,1,0,0,1,2,1,1,0,2,2,1,2,1,2,1,0,0,0,1,2,0,2,2,0,1],[1,2,1,0,0,1,1,1,0,2,0,0,0,1,2,2,2,2,2,0,0,1,1,0,1,1,0,1,0,1,2,2,0,0,2,1,1,0,1,0,1,1,2,1,0,0,0,0,0,1,1,1],[2,1,1,2,0,0,2,0,2,0,2,2,2,0,2,1,0,2,2,1,2,0,1,2,1,2,2,1,2,0,0,2,2,0,2,1,2,0,0,0,0,2,0,1,2,1,1,2,1,2,0,0],[2,2,1,2,1,2,2,0,0,1,1,1,0,0,1,2,1,2,0,1,1,0,1,1,2,0,0,0,1,2,1,1,0,2,1,0,0,1,1,0,1,1,1,0,0,2,0,0,0,1,0,0],[2,0,2,0,0,0,1,1,2,1,0,1,1,1,1,1,2,0,1,1,1,0,1,2,1,2,0,1,1,0,0,1,2,1,1,1,2,1,1,2,1,1,0,0,1,1,0,1,0,0,1,0],[0,2,1,1,1,1,2,1,2,1,0,0,0,1,0,0,1,1,0,0,2,1,1,0,0,2,2,1,2,2,0,1,0,2,2,0,2,0,2,2,0,2,0,2,1,1,2,1,1,2,2,0],[2,0,2,2,2,2,2,1,0,0,2,0,2,2,1,2,0,2,2,0,0,2,1,2,2,2,2,0,0,1,1,0,2,1,1,0,0,0,2,1,1,0,0,0,1,2,1,1,0,2,2,1],[1,2,1,2,2,0,1,1,2,1,1,2,0,1,1,1,1,0,2,0,2,0,0,0,1,2,1,1,0,2,0,0,0,0,1,1,1,2,2,0,0,2,0,1,1,0,1,2,0,2,2,2],[1,1,0,0,1,2,0,1,1,0,1,0,2,0,0,0,0,2,0,0,0,2,2,2,1,2,1,1,1,0,2,0,0,2,1,2,0,0,1,2,2,0,1,1,0,1,1,2,0,2,2,2],[0,0,0,2,0,2,2,2,2,0,1,0,2,2,0,2,1,1,1,1,1,0,0,0,0,0,0,1,2,0,2,2,2,0,0,1,0,1,1,1,2,1,0,2,2,2,2,1,1,2,1,1],[0,1,1,2,0,2,2,2,1,2,1,0,1,1,0,0,0,0,2,0,1,1,0,0,2,1,1,1,2,0,2,1,1,0,0,1,1,0,2,0,1,2,1,2,0,0,0,1,0,0,2,2],[2,2,2,0,2,0,1,0,0,1,1,0,2,2,2,2,1,0,2,1,0,1,2,2,2,2,1,2,1,1,0,2,1,2,1,0,0,2,1,2,1,0,2,2,2,0,1,0,0,2,0,1],[1,2,0,2,2,1,1,0,0,1,0,1,0,1,0,1,1,0,2,1,1,0,1,2,0,1,2,2,1,2,1,1,0,1,0,0,0,0,0,0,0,1,1,0,2,0,0,0,0,0,2,2],[2,1,0,0,2,1,0,1,0,0,0,1,1,0,0,1,1,0,1,0,2,1,0,1,1,2,0,0,1,2,0,2,2,1,0,2,0,2,0,1,2,1,2,1,0,1,1,1,2,2,1,0],[0,2,2,0,0,1,1,1,2,0,1,0,2,0,1,0,1,1,0,0,2,0,1,0,0,0,1,1,2,0,1,2,0,2,1,2,0,0,0,2,1,0,2,1,2,0,0,0,0,0,1,1],[1,2,0,1,0,2,1,2,0,0,1,2,2,0,1,2,0,2,0,1,0,2,2,2,0,1,1,0,0,1,1,1,1,1,0,1,2,2,2,2,0,2,2,2,2,2,0,1,0,1,2,0],[0,1,2,0,2,2,2,0,1,0,1,1,2,1,1,2,0,1,2,2,1,1,0,1,2,1,1,1,2,0,2,0,2,0,2,1,0,1,1,2,2,1,2,0,0,2,1,1,2,1,2,1],[2,2,2,2,1,2,0,2,2,0,0,1,2,1,1,2,2,0,0,1,1,2,2,1,0,1,2,1,1,0,1,2,1,2,0,1,0,2,2,1,0,0,1,1,2,2,2,2,1,0,0,1],[0,0,1,1,0,0,0,1,2,0,0,1,2,2,1,1,0,0,1,1,2,1,2,1,2,1,1,1,1,2,0,1,1,0,1,1,0,0,1,2,0,1,2,0,0,2,1,2,1,1,2,0],[0,0,1,1,1,2,2,0,0,2,1,1,0,2,0,2,0,0,0,2,0,2,2,0,2,1,1,2,0,0,1,1,1,1,1,1,1,0,2,0,2,0,2,2,0,0,0,1,1,1,1,2],[0,2,0,0,1,1,1,0,1,2,0,2,2,2,2,2,0,1,1,1,2,2,1,1,1,0,0,0,2,2,0,0,1,0,1,2,1,2,1,2,1,2,2,0,1,0,0,2,1,1,2,1],[0,2,0,0,1,2,2,1,1,1,2,0,2,1,1,0,1,1,1,1,2,0,1,1,1,1,0,0,1,2,1,0,2,2,2,1,1,2,0,0,1,1,0,2,1,1,0,0,1,0,0,2],[1,0,2,0,1,2,2,0,2,0,0,0,1,2,2,2,1,0,1,1,0,0,0,2,0,0,2,2,0,2,0,0,2,0,0,2,2,1,1,1,0,1,0,2,2,0,0,2,1,0,0,0],[0,0,1,2,0,2,2,2,2,0,0,1,1,2,2,1,1,1,0,1,0,2,0,2,2,1,0,1,2,1,2,0,0,2,2,1,1,2,2,1,2,1,0,0,0,1,0,2,0,1,0,2],[1,1,1,0,0,2,1,1,2,2,2,2,2,1,0,2,0,2,0,0,1,0,0,0,0,0,0,2,1,1,0,0,2,1,1,2,2,1,0,0,0,2,1,0,1,2,0,2,1,0,0,0],[1,0,2,1,1,1,1,0,1,1,1,2,2,2,1,0,2,2,1,2,1,0,2,1,0,1,1,2,1,0,0,2,2,1,2,0,2,1,1,0,0,1,2,1,1,2,2,0,2,0,2,1],[1,0,2,2,0,2,1,0,0,2,1,0,2,0,2,1,2,2,1,1,0,1,0,1,0,2,1,1,1,2,0,2,2,1,1,2,2,0,1,2,2,0,1,2,1,0,1,2,1,1,0,1],[0,1,0,1,0,1,1,1,0,1,1,0,2,2,1,0,2,2,1,0,0,2,0,2,0,0,1,2,1,0,0,1,0,0,2,2,2,2,0,0,1,2,0,1,0,2,1,2,0,2,0,2],[2,2,2,1,2,2,1,1,0,2,1,1,0,0,0,0,1,2,1,0,1,1,1,2,2,0,0,1,1,0,0,1,2,0,2,0,0,2,1,0,1,2,0,2,1,2,0,2,1,1,1,1],[1,1,1,2,2,1,2,0,2,0,1,2,1,1,2,2,0,0,0,0,0,0,2,0,1,2,1,1,0,2,2,2,0,2,2,1,1,1,1,1,0,2,1,1,1,2,0,2,0,1,2,0],[0,1,2,1,2,2,2,2,2,0,1,2,2,2,1,0,1,2,2,1,1,2,0,0,1,0,0,1,1,0,1,0,2,2,2,2,1,0,2,0,2,1,0,2,0,1,0,0,2,0,2,2],[1,1,1,1,2,1,2,0,1,2,0,2,1,1,1,1,0,2,0,1,1,1,1,0,0,0,2,0,1,2,0,2,0,1,0,2,0,2,2,1,0,0,2,1,2,0,2,0,2,1,2,0],[0,1,2,2,0,1,2,1,1,0,1,1,2,2,0,0,1,1,2,1,0,2,0,2,0,1,0,2,1,0,1,1,1,0,1,2,0,0,2,1,1,0,0,1,0,0,1,2,1,2,1,2],[0,1,1,2,1,0,1,2,0,1,0,1,0,1,1,2,2,1,0,0,2,2,2,0,1,0,1,1,2,0,0,1,0,1,0,2,2,1,1,1,2,2,1,2,2,2,1,1,1,0,0,2],[2,1,1,1,0,0,0,2,0,2,2,2,0,0,1,0,0,1,2,1,1,0,0,2,0,1,0,2,1,2,0,2,0,1,1,2,1,1,0,0,1,2,1,0,0,2,0,2,0,1,1,2],[0,2,2,2,1,1,0,0,0,1,0,2,2,0,1,0,2,0,1,1,2,1,0,2,0,2,2,1,1,2,2,0,0,1,0,1,0,2,2,1,0,2,1,1,2,1,0,1,0,0,0,2],[2,0,1,2,2,1,1,2,1,0,2,2,0,1,2,2,1,1,0,1,0,0,2,1,2,2,2,2,2,0,0,2,2,2,0,0,0,0,0,2,2,1,0,0,2,0,1,0,2,0,0,0],[2,2,2,2,1,1,2,2,2,1,0,0,1,1,0,1,2,0,1,2,1,0,2,2,0,2,1,1,0,2,2,1,0,2,0,0,2,2,2,0,1,0,1,1,1,0,2,0,0,1,0,0],[1,2,0,0,0,1,2,0,1,1,1,1,1,0,1,0,0,2,1,1,0,0,1,1,2,1,0,1,0,0,2,1,1,2,1,0,1,0,1,0,1,1,0,0,0,2,1,2,1,1,2,1],[0,1,0,0,1,2,0,2,2,2,0,2,1,1,2,1,0,2,2,0,0,0,2,2,1,2,0,0,2,1,1,0,2,0,0,0,2,0,2,0,1,0,1,1,1,1,1,2,1,2,0,2],[2,2,0,0,2,2,2,0,1,1,1,1,0,0,2,2,0,1,0,1,0,2,1,0,2,2,0,1,1,0,1,0,1,0,1,0,2,1,1,0,1,0,1,2,0,1,2,0,0,0,1,1],[0,2,1,2,0,0,2,1,1,0,1,2,1,2,0,0,0,1,1,2,1,2,0,0,2,2,2,2,0,1,0,0,1,1,0,1,0,2,1,1,1,0,0,0,0,1,1,2,2,1,1,1],[1,2,1,0,0,0,2,2,0,0,0,0,0,2,1,2,2,1,1,2,0,0,1,0,1,0,2,0,2,2,2,0,0,1,0,1,1,2,2,0,1,2,2,1,1,2,2,1,1,2,1,1],[0,2,0,2,0,1,1,2,0,1,0,2,2,2,1,1,1,2,0,0,2,0,0,2,0,0,2,0,1,0,0,1,1,2,1,0,2,0,1,1,1,1,1,0,2,1,0,2,2,1,2,0],[2,2,2,1,0,0,2,2,0,1,2,2,2,2,2,1,0,2,2,0,1,1,2,2,1,1,2,2,1,0,0,0,0,1,0,2,0,0,2,1,1,2,1,1,0,0,2,0,2,0,2,1],[2,0,1,1,1,1,1,2,2,0,2,0,1,1,0,2,1,2,1,1,0,0,0,2,1,0,2,1,2,0,1,2,1,2,0,0,1,1,2,2,2,1,2,2,0,2,0,0,2,1,2,1],[0,2,0,1,0,0,2,1,0,2,0,2,1,2,0,2,0,0,2,0,0,0,0,1,0,0,1,1,1,2,0,2,2,1,0,1,1,0,1,0,1,0,1,2,1,0,2,2,0,2,0,2],[0,1,2,2,2,2,2,0,0,0,2,0,1,2,0,0,2,2,0,2,2,0,1,2,2,0,1,2,1,0,1,2,1,1,1,2,1,0,1,0,1,0,2,2,1,2,0,0,2,2,1,0],[0,2,1,2,0,2,0,2,2,1,0,1,2,1,2,0,1,2,0,0,0,2,1,0,2,1,1,2,2,0,1,0,1,2,1,1,0,1,0,0,2,1,1,2,1,1,0,1,1,1,1,1],[1,1,0,0,2,2,0,0,2,1,2,0,1,2,1,2,1,2,0,0,2,1,0,2,0,2,2,2,0,2,2,1,1,0,1,2,0,1,0,1,2,2,2,1,2,2,1,2,1,2,1,2],[1,1,0,1,2,1,2,2,2,2,2,1,2,1,0,1,0,0,2,1,0,0,0,1,0,2,2,1,1,0,2,1,1,0,0,0,1,0,1,2,1,0,0,1,0,1,1,2,1,0,0,2],[1,2,1,2,0,2,2,2,0,1,0,2,2,0,1,1,2,0,0,0,0,1,2,2,0,0,2,0,0,2,1,1,0,2,0,0,0,1,2,0,1,1,2,1,0,1,1,0,0,0,2,1],[2,0,1,1,2,2,2,0,1,2,0,2,0,1,2,1,1,0,1,0,0,2,2,0,0,2,2,1,0,2,1,0,2,0,2,0,1,0,0,2,2,2,1,1,0,2,2,0,1,2,0,0],[0,1,0,0,2,2,0,1,0,2,1,1,0,0,2,0,2,2,2,1,2,0,2,1,1,1,0,0,2,0,0,2,2,0,1,1,1,0,1,0,2,0,0,1,2,2,2,2,2,1,0,1],[2,2,1,0,1,0,1,2,2,1,1,1,1,0,0,1,0,2,0,0,0,0,0,1,0,2,1,1,1,0,2,0,1,1,2,1,2,0,2,2,1,2,1,2,2,0,2,0,2,1,0,1],[0,2,0,0,2,2,1,2,1,2,1,1,2,2,1,2,1,1,0,2,2,0,0,1,0,2,0,1,0,0,1,2,0,2,1,1,1,2,0,0,2,0,2,0,0,2,1,0,2,0,1,2],[2,1,1,0,2,2,1,1,2,0,0,2,1,0,0,0,0,1,1,0,2,1,2,0,2,2,0,2,1,1,1,2,2,0,1,0,2,2,0,0,0,1,2,1,1,1,2,2,0,2,2,2],[0,0,2,1,2,1,1,2,0,2,1,2,0,0,1,1,0,0,2,2,2,2,2,0,1,1,2,1,2,0,2,0,0,2,0,0,0,1,1,1,2,0,1,2,1,0,2,1,2,1,2,1],[2,0,0,2,0,1,0,2,1,0,0,0,2,2,1,1,0,1,1,0,1,1,2,1,2,2,0,0,0,1,2,0,1,1,0,0,2,0,0,1,2,0,0,1,1,1,0,2,2,0,2,2],[1,1,2,2,1,2,0,1,1,0,2,2,0,2,1,0,1,2,0,1,1,2,2,1,0,0,0,1,1,0,2,2,1,1,2,1,1,1,2,2,0,2,0,0,1,2,0,2,1,1,2,0],[2,1,1,1,2,1,1,2,2,0,1,1,2,0,0,0,1,2,2,0,0,2,0,0,2,1,0,2,2,2,0,2,1,1,0,1,0,0,1,1,0,2,2,2,2,2,0,0,1,1,2,0],[0,2,1,2,0,0,0,1,2,1,0,0,0,0,0,0,2,1,1,1,0,2,1,2,2,0,2,1,1,2,1,2,1,0,1,0,2,0,0,2,0,2,1,1,0,0,1,0,0,0,2,0],[1,0,2,2,2,2,0,0,1,2,0,1,0,1,2,0,0,2,1,1,0,1,1,2,1,2,1,1,0,0,0,2,0,2,2,1,2,2,1,2,0,2,2,0,0,2,2,0,0,0,0,1],[1,0,2,1,1,0,1,1,0,2,2,0,1,0,1,0,2,1,0,0,2,1,0,0,2,2,1,0,1,2,0,2,0,0,1,1,0,0,1,2,0,2,2,2,0,2,0,1,1,1,1,0],[2,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,2,2,2,0,0,2,0,2,2,2,1,1,0,0,0,2,1,2,0,2,1,0,2,0,1,0,2,2,0,1,0,2,2,2,1,2],[1,1,2,2,2,2,0,0,2,2,0,0,0,0,2,1,0,1,0,1,1,0,0,2,1,2,2,1,1,1,1,2,0,1,1,1,2,1,1,0,1,1,1,0,1,2,2,1,0,2,2,1],[1,0,1,2,2,0,1,0,1,2,1,1,2,0,0,1,2,2,1,2,2,1,2,2,1,2,1,2,0,0,0,2,1,2,1,2,0,2,1,2,1,2,0,0,0,2,2,2,0,1,0,1],[2,2,1,0,0,1,2,0,2,1,0,2,0,0,2,2,2,0,0,2,1,1,0,1,1,2,2,1,0,0,2,0,2,1,2,2,1,1,0,1,0,2,0,2,0,2,2,2,2,2,0,1],[0,2,0,1,2,2,2,2,0,1,2,2,2,1,0,1,1,2,1,0,1,0,0,1,0,1,1,1,1,2,2,1,0,0,2,0,1,0,0,2,1,0,0,1,1,2,0,1,2,0,0,2]]))