"""
130. Surrounded Regions

    Total Accepted: 64206
    Total Submissions: 378992
    Difficulty: Medium

Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
import collections
class Solution(object):
    def solve(self, board):
        """
        :type bd: List[List[str]]
        :rtype: void Do not return anything, modify bd in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0: return
        queue = collections.deque([])
        
        h, w = len(board)-1, len(board[0])-1

        for r in xrange(h+1):
            if board[r][0] == "O": queue.append((r, 0))
            if board[r][w] == "O": queue.append((r, w))

        for c in xrange(w+1):
            if board[0][c] == "O": queue.append((0, c))
            if board[h][c] == "O": queue.append((h, c))

        while queue:
            r, c = queue.popleft()
            if 0<=r<=h and 0<=c<=w and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))
            
        for r in xrange(h+1):
            for c in xrange(w+1):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"