"""
1254
"""
from typing import List
class Solution:
    def closedIsland(self, A: List[List[int]]) -> int:
        # 1. first differentiate islands and all non-island-0s
        # 2. count the number of islands

        # print('befor',A)
        def diff(i, j):
            if A[i][j] == 1: return
            A[i][j] = 1
            if i+1 < len(A):
                diff(i+1, j)
            if i-1 >= 0:
                diff(i-1, j)
            if j+1 < len(A[0]):
                diff(i, j+1)
            if j-1 >= 0:
                diff(i, j-1)
            return

        for i in range(len(A)):
            diff(i, 0)
            diff(i, len(A[0])-1)
        
        for j in range(len(A[0])):
            diff(0, j)
            diff(len(A)-1, j)

        self.count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    self.count += 1
                    diff(i, j)
        # print('fin',A)

        return self.count
    
print(Solution().closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
print(Solution().closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
print(Solution().closedIsland([[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]))