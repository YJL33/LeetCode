from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # first pass: mark those edge-regions (and its connected regions)
        # 2nd pass: flip those surrounded regions
        # flip those back.

        def mark(i, j, before, after):
            board[i][j] = after
            for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=a<H and 0<=b<W and board[a][b] == before:
                    mark(a,b,before,after)
            return


        H, W = len(board), len(board[0])
        for i in range(H):
            if board[i][0] == 'O': mark(i, 0, 'O', 'E')
            if board[i][W-1] == 'O': mark(i, W-1, 'O', 'E')
        
        for j in range(W):
            if board[0][j] == 'O': mark(0, j, 'O', 'E')
            if board[H-1][j] == 'O': mark(H-1, j, 'O', 'E')
        
        for i in range(H):
            for j in range(W):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == 'E': board[i][j] = 'O'

        return