"""
https://leetcode.com/problems/design-tic-tac-toe/
"""
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.size = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # for each move, check its row/col/diag is occupied or not
        self.board[row][col] = player
        if self.checkRow(row, col): return player
        if self.checkCol(row, col): return player
        if self.checkDiag1(row, col): return player
        if self.checkDiag2(row, col): return player
        return 0
    
    def checkRow(self, r, c):
        x = self.board[r][c]
        for b in self.board[r]:
            if b != x: return False
        return True
    
    def checkCol(self, r, c):
        x = self.board[r][c]
        for row in self.board:
            b = row[c]
            if b != x: return False
        return True
    
    def checkDiag1(self, r, c):
        if r!=c: return False
        x, n = self.board[r][c], self.size
        for i in range(n):
            b = self.board[i][i]
            if b != x: return False
        return True

    def checkDiag2(self, r, c):
        if r+c!=self.size-1: return False
        x, n = self.board[r][c], self.size
        for i in range(n):
            b = self.board[i][n-1-i]
            if b != x: return False
        return True


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)