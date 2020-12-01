"""
https://leetcode.com/problems/game-of-life/
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        new = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                liveCnt = 0
                for p in range(max(0, i-1), min(i+2, len(board))):
                    for q in range(max(0, j-1), min(j+2, len(board[0]))):
                        liveCnt += board[p][q]
                # live-dead logic
                if board[i][j]:
                    if liveCnt-1 in [2,3]: new[i][j] = 1
                else:
                    if liveCnt == 3: new[i][j] = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = new[i][j]
        return

print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]), Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]) == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])