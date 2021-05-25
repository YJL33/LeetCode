"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

A sudoku puzzle...

...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

Accepted 179.2K
Submissions 422.8K
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def dfs():
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        # fill the spot with available numbers
                        p, q = i//3, j//3
                        availables = set9 - {board[i][r] for r in xrange(9)} - {board[c][j] for c in xrange(9)} - {board[x][y] for x in xrange(3*p, 3*(p+1)) for y in xrange(3*q, 3*(q+1))}
                        
                        for n in availables:
                            board[i][j] = n

                            if dfs():
                                return True
                            else:
                                board[i][j] = '.'

                        return False
            return True

        set9 = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        dfs()
        
        # print board

print Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])