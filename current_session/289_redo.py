"""
289
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # rules
        '''
        Any live cell with <2 live neighbors dies, as if caused by under-population.
        Any live cell with 2 or 3 live neighbors lives on to the next generation.
        Any live cell with >3  live neighbors dies, as if by over-population.
        Any dead cell with ==3 live neighbors becomes a live cell, as if by reproduction.
        '''
        nbs = [(1,0),(-1,0),(1,1),(-1,-1),(0,1),(0,-1),(1,-1),(-1,1)]
        nxt = [[-1 for _ in range(board[0])] for _ in range(board)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                liveCnt = 0
                for n in nbs:
                    if 0<=i+n[0]<len(board) and 0<=j+n[1]<len(board[0]):
                        liveCnt += board[i+n[0]][j+n[1]]
                if board[i][j] == 1:
                    nxt[i][j] = 1 if liveCnt in (2,3) else 0
                else:
                    nxt[i][j] = 1 if liveCnt == 3 else 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = nxt[i][j]

        return