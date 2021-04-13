"""
529
"""
from typing import List
class Solution:
    def count(self, board, i, j):
        nbs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        cnt = 0
        for a,b in nbs:
            if 0<=i+a<len(board) and 0<=j+b<len(board[0]) and board[i+a][j+b] == 'M':
                cnt += 1
        return cnt

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 1st pass: see if it's gonna bomb or not
        # 
        # 2nd pass: generate number and blank
        #           see if it's on a number or not
        #           if it's on a blank, reveal blank first and reveal number as well

        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        cntAtClick = self.count(board, i, j)
        if cntAtClick == 0:
            # reveal all connected '0's and numbers as well
            st = [(i,j)]
            toChange = []
            # print(board)
            visited = set()
            while st:
                p, q = st.pop()
                visited.add((p,q))
                # print('p,q:',p,q)
                cnt = self.count(board, p, q)
                if cnt == 0:
                    toChange += (p, q, 'B'),
                    for a, b in [(p+1,q),(p-1,q),(p,q+1),(p,q-1),(p+1,q+1),(p+1,q-1),(p-1,q+1),(p-1,q-1)]:
                        if 0<=a<len(board) and 0<=b<len(board[0]) and (a,b) not in visited:
                            st.append((a,b))
                else:
                    toChange += (p, q, str(cnt)),
            
            while toChange:
                r, c, val = toChange.pop()
                board[r][c] = val
            return board
        
        else:
            board[i][j] = str(cntAtClick)
            return board
