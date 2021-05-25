"""
289. Game of Life

According to the Wikipedia's article:
"The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells,
each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time:
    You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array.
    In principle, the board is infinite,
    which would cause problems when the active area encroaches the border of the array.
    How would you address these problems?
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # Return next status based on a cell's neighbors, according to it's alive or dead.
        # If alive: check the number of alive neighbors == 2 or 3 or not.
        # If dead: check the number of alive neighbors == 3 or not

        width = len(board[0])         # width of board
        height = len(board)           # height of board
        
        # Use a new matrix to record the next state
        new = [[0 for _ in xrange(width)] for _ in xrange(height)]
        
        for i in xrange(height):            # vertical iterator
            for j in xrange(width):         # horizontal iterator
                num_of_alives = 0
                for y in xrange(max(0,i-1), min(height,i+2)):       # vertical => y
                    for x in xrange(max(0,j-1), min(width,j+2)):    # horizontal => x
                        if (i,j) != (y,x) and board[y][x] == 1:
                            num_of_alives += 1                      # count the number
                if board[i][j] and abs(num_of_alives-2.5) < 1:
                    new[i][j] = 1
                if not board[i][j] and num_of_alives == 3:
                    new[i][j] = 1

        for i in xrange(height):
            for j in xrange(width):
                board[i][j] = new[i][j]                             # update the board

        return