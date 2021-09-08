from typing import List

class NumMatrix:

    # prepare a sum matrix where p = (x, y) = sumRegion of (0,0), (x,y)
    def __init__(self, matrix: List[List[int]]):
        H, W = len(matrix), len(matrix[0])
        self.A = [[0 for _ in range(W)] for _ in range(H)]
        self.A = matrix[0][0]
        for i in range(1,H):
            self.A[i][0] = self.A[i-1][0] + matrix[i][0]
        for j in range(1,W):
            self.A[0][j] = self.A[0][j-1] + matrix[0][j]
        for i in range(1,H):
            for j in range(1,W):
                self.A[i][j] = matrix[i][j] + self.A[i-1][j] + self.A[i][j-1] - self.A[i-1][j-1]

    # leverage sumMatrix, say p=(x,y), f(x,y) = sumMatrix of (x,y)
    # e.g. say, given a = (3,3), b = (5,5), then the answer = f(5,5) + f(2,2) - f(2,5) - f(5,2)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.A[row2][col2]
        b = self.A[row2][col1-1] if col1 >= 1 else 0
        c = self.A[row1-1][col2] if row1 >= 1 else 0
        d = self.A[row1-1][col1-1] if (col1 >= 1 and row1 >= 1) else 0
        return a-b-c+d

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)