"""
723
"""
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        def markIt(bd, i, j, cnt, vert=True):
            if vert:
                if cnt == 3:
                    bd[i][j] = 1
                    bd[i+1][j] = 1
                    bd[i+2][j] = 1
                else:
                    bd[i][j] = 1
            else:
                if cnt == 3:
                    bd[i][j] = 1
                    bd[i][j-1] = 1
                    bd[i][j-2] = 1
                else:
                    bd[i][j] = 1
            return bd
        
        # scan the board (vertically then horizontally)
        stable = True
        toCrush = [[0 for _ in board[0]] for _ in board]
        for col in range(len(board[0])):
            prev, cnt = board[-1][col], 0
            for row in range(len(board)-1,-1,-1):   # bottom-up
                if board[row][col] == 0:
                    break
                if board[row][col] == prev:
                    cnt += 1
                    if cnt >= 3:
                        stable = False
                        toCrush = markIt(toCrush, row, col, cnt)
                else:
                    prev, cnt = board[row][col], 1
        
        # horizontally
        for i in range(len(board)-1,-1,-1):
            prev, cnt = board[i][0], 0
            for j in range(len(board[0])):
                if board[i][j] == prev and board[i][j] != 0:
                    cnt += 1
                    if cnt >= 3:
                        stable = False
                        toCrush = markIt(toCrush, i, j, cnt, False)
                else:
                    prev, cnt = board[i][j], 1
        
        # crush the candy based on mark and re-construct the board
        tmp = [[0 for _ in board[0]] for _ in board]
        cur = [0 for _ in range(len(board[0]))]     # the amount shift upward
        for i in range(len(board)-1,-1,-1):
            for j in range(len(board[0])):
                if i-cur[j] < 0:
                    continue
                while toCrush[i-cur[j]][j] == 1 and i-cur[j] >= 0:
                    cur[j] += 1
                if i-cur[j] >= 0:
                    tmp[i][j] = board[i-cur[j]][j]
        
        return board if stable else self.candyCrush(tmp)

print(Solution().candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))

print [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]