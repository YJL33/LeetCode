"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
"""
class Solution(object):
    """ Solution of LEETCODE #37 """
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs():
            for i, row in enumerate(board):
                for j, char in enumerate(row):
                    if char == '.':
                        for x in s9 - {row[k] for k in r9} - {board[k][j] for k in r9} - \
                        {board[i / 3 * 3 + m][j / 3 * 3 + n] for m in r3 for n in r3}:
                            board[i][j] = x
                            if dfs(): return True
                            board[i][j] = '.'
                        return False
            return True

        r3, r9, s9 = range(3), range(9), {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        dfs()