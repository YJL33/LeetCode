"""
36
"""
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check: horizontal / vertical / box
        H, W = len(board), len(board[0])
        def checker(r, c):
            x = board[r][c]
            for i in range(H):
                if board[i][c] == x and i != r:
                    return False
            for j in range(W):
                if board[r][j] == x and j != c:
                    return False
            a, b = 3*(r//3), 3*(c//3)
            for i in range(3):
                for j in range(3):
                    if a+i == r and b+j == c:
                        continue
                    if board[a+i][b+j] == x:
                        return False
            return True


        for i in range(H):
            for j in range(W):
                if board[i][j] == '.':
                    continue
                if not checker(i, j):
                    return False
        return True