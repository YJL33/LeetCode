"""
59
"""
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # fill the matrix
        cd, d = [[0,1],[1,0],[0,-1],[-1,0]], 0       # cardinal direction
        i, j, x = 0, 0, 1
        arr = [[-1 for _ in range(n)] for _ in range(n)]
        while x <= n*n:
            arr[i][j] = x
            x += 1
            dx, dy = cd[d][0], cd[d][1]
            if not (0 <= i+dx < n and 0 <= j+dy < n) or arr[i+dx][j+dy] != -1:
                d = (d+1)%4
                dx, dy = cd[d][0], cd[d][1]
            i, j = i+dx, j+dy

        return arr

print(Solution().generateMatrix(4))
print(Solution().generateMatrix(3))
print(Solution().generateMatrix(2))
print(Solution().generateMatrix(1))