"""
419
"""
from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        H, W = len(board), len(board[0])
        def sink(i, j):
            board[i][j] = '.'
            # check vertical
            while i+1<H and board[i+1][j] == 'X':
                board[i+1][j] = '.'
                i += 1
            while j+1<W and board[i][j+1] == 'X':
                board[i][j+1] = '.'
                j += 1
            # for a, b in [(i+1,j), (i,j+1)]:
            #     if 0<=a<H and 0<=b<W and board[a][b] == 'X':
            #         sink(a,b)
            return

        cnt = 0
        for i in range(H):
            for j in range(W):
                if board[i][j] == 'X':
                    cnt += 1
                    sink(i, j)
        return cnt

print(Solution().countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print(Solution().countBattleships([["X","X","X"]]))
