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
        def has_answer(row, col):
            """ Check whether this location can put answer inside"""
            ref_dict = {}      # Dictionary for any location, including its reference neighbors
            ref_dict["."] = 1
            for i in xrange(9):
                if board[row][i] not in ref_dict and board[row][i] is not '.':
                    ref_dict[board[row][i]] = 1
                if board[i][col] not in ref_dict and board[i][col] is not '.':
                    ref_dict[board[i][col]] = 1
            for i in xrange(3):
                for j in xrange(3):
                    ref_r = (row//3)*3 + i
                    ref_c = (col//3)*3 + j
                    if board[ref_r][ref_c] not in ref_dict and board[ref_r][ref_c] is not '.':
                        ref_dict[board[ref_r][ref_c]] = 1
            if len(ref_dict) != 9:
                return False
            for cand in '123456789':
                if cand not in ref_dict:
                    board[row] = bool(col!=0)*board[row][:col] + str(cand) + bool(col!=8)*board[row][col+1:]
            return True

        def put_answer(board):
            """ Put the only answer into the location """
            count = 0
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == "." and has_answer(i, j):
                        count += 1
            if count == 0:
                return False
            else:
                return True

        while put_answer(board):
            pass
        return board
