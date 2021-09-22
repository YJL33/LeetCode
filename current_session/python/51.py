# use DFS

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = self.craftEmptyBoard(n)
        res = []
        self.dfs(res, board, 0)
        return res

    # dfs: trying all empty spots, if invalid => return
    # we can try row by row, i=row index
    def dfs(self, result, board, i):
        # termination
        if i == len(board):
            result.append([''.join(r) for r in board])
            return
        row = board[i]
        for j in range(len(row)):
            if self.verifyBoard(board, i, j):
                board[i][j] = 'Q'
                self.dfs(result, board, i+1)
                # restore the board
                board[i][j] = '.'
        return
    
    def verifyBoard(self, board, i, j):
        for r in range(len(board)):
            if board[r][j] == 'Q':
                return False
        for c in range(len(board[0])):
            if board[i][c] == 'Q':
                return False
        # verify 45-deg / 135-deg
        for p in range(len(board)):
            for q in range(len(board[0])):
                if (p+q) == (i+j) and p!=i and board[p][q] == 'Q':
                    return False
                if p-q == i-j and board[p][q] == 'Q':
                    return False
        return True

    # craft an empty board
    def craftEmptyBoard(self, n):
        return [["."]*n for _ in range(n)]

print(Solution().solveNQueens(4))