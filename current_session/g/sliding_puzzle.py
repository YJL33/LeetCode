from typing import List
import collections
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # bfs, set a max threshold
        # return count when the board is as same as target
        dq = collections.deque()
        dq.append((board, 0))
        seen = set()
        
        seen.add(self.hashBoard(board))

        # self.swap(board, 1, 1, 0, 1)

        while dq:
            bd, mv = dq.popleft()
            # if mv >= 100: return -1
            if self.isFinal(bd): return mv

            i, j = self.findZero(bd)
            for a, b in [(i+1,j), (i-1,j), (i,j+1),(i,j-1)]:
                if 0<=a<2 and 0<=b<3:
                    newBd = self.swap(bd, i, j, a, b)
                    hashedNewBd = self.hashBoard(newBd)
                    if hashedNewBd not in seen:
                        seen.add(hashedNewBd)
                        dq.append((newBd, mv+1))
            # print('dq:', dq)
        return -1


    def hashBoard(self, bd):
        return ''.join([''.join([str(a) for a in r]) for r in bd])
    
    def swap(self, bd, i, j, a, b):
        # print('bd:', bd)
        # print('i,j,c,d',i,j,a,b)
        newBoard = [[x for x in row] for row in bd]
        newBoard[i][j], newBoard[a][b] = newBoard[a][b], newBoard[i][j]
        # print('n:', newBoard)
        return newBoard

    def isFinal(self, board):
        # print('bd:',board)
        if board[0][0] != 1 or board[0][1] != 2 or board[0][2] != 3 or board[1][0] != 4 or board[1][1] != 5 or board[1][2] != 0: return False
        return True
        
    
    def findZero(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0: return i, j

print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))
print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))
print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))
print(Solution().slidingPuzzle([[3,2,4],[1,5,0]]))