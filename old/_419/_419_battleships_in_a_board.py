"""
419. Battleships in a Board

    Total Accepted: 145
    Total Submissions: 314
    Difficulty: Medium
    Contributors: ben65

Given an 2D board, count how many different battleships are in it.
The battleships are represented with 'X's, empty slots are represented with '.'s.
You may assume the following rules:

    You receive a valid board, made of only battleships or empty slots.
    Battleships can only be placed horizontally or vertically.
    Battleships come in different sizes.
    At least one space of horizontal or vertical separates between two battleships
    - no adjacent battleships will be given.

Example:

X..X
...X
...X

In the above board there are 2 battleships.

Your algorithm should not modify the value of the board.
"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def checkNeighbors(row, col):
            if labels[row][col-1] or labels[row-1][col]:
                return labels[row][col-1] or labels[row-1][col]
            return None

        height, width, count = len(board), len(board[0]), 0
        labels = [[0 for _ in xrange(width)] for _ in xrange(height)]
        for row in xrange(height):
            for col in xrange(width):
                if board[row][col] == 'X':
                    if checkNeighbors(row, col):
                        labels[row][col] = checkNeighbors(row, col)
                    else:
                        count += 1
                        labels[row][col] = count
        return count