# capture all edge 'O's
# convert all other grids to 'X'
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        H, W = len(board), len(board[0])

        # mark this grid and all its related 'O' as boarder-'O' (e.g. "B")
        def mark(i, j):
            board[i][j] = "B"
            for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=a<H and 0<=b<W and board[a][b] == 'O':
                    mark(a, b)
            return

        # search left and right boarder
        for i in range(H):
            for j in (0, W-1):
                if board[i][j] == "O": mark(i, j)
        
        # search top and bottom boarder
        for j in range(W):
            for i in (0,H-1):
                if board[i][j] == "O": mark(i,j)
        
        # print('after mark:', board)

        # boarder-O => O, else => X
        def convert():
            for i in range(H):
                for j in range(W):
                    if board[i][j] == "B": board[i][j] = "O"
                    else: board[i][j] = "X"
            return
        
        convert()
        # print('after convert:', board)
        return

print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(Solution().solve([["X"]]))
# print(Solution().solve())

        