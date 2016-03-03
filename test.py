"""
General testing model for LEETCODE
"""
import sys
#import _264_ugly_numbers_2 as mod
import _36_valid_sudoku as mod

board = ["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
"""
[["5", "3", ".", ".", "7", ".", ".", ".", "."],
		 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
		 [".", "9", "8", ".", ".", ".", ".", "6", "."],
		 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		 [".", "6", ".", ".", ".", ".", "2", "8", "."],
		 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
		 [".", ".", ".", ".", "8", ".", ".", "7", "9"],]
		 """
sol = mod.Solution()
sol.isValidSudoku = mod.Solution.isValidSudoku(sol, board)
print sol.isValidSudoku
