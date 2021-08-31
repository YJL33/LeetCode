from typing import List
class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for c in col:
            for i in range(len(A)):
                A[i][c] = 0
        
        for r in row:
            for j in range(len(A[0])):
                A[r][j] = 0
        
        return

