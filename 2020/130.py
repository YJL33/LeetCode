"""
130
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        H, W = len(board), len(board[0])
        def sink(i,j):
            board[i][j] = 'V'
            nb = [(0,1),(0,-1),(1,0),(-1,0)]
            for x,y in nb:
                ii, jj = i+x, j+y
                if 0<=ii<H and 0<=jj<W and board[ii][jj] == 'O':
                    sink(ii, jj)
            return                    

        # 1. mark the 'o' grids from the edge (as 'v' )
        # 2. mark all 'o' to 'x'
        for i in range(H):
            for j in (0,W-1):
                if board[i][j] == 'O':
                    sink(i,j)
        for j in range(W):
            for i in (0, H-1):
                if board[i][j] == 'O':
                    sink(i,j)
        
        for i in range(H):
            for j in range(W):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'
        return
        
