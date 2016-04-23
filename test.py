"""
General testing model for LEETCODE
"""
import sys
#import _264_ugly_numbers_2 as mod
#import _137_single_number_2 as mod137
#import _36_valid_sudoku as mod36
import _30_substring_with_concatenation_of_all_words as mod30

#sol137 = mod137.Solution()
#quest = [3, 3, 3, 1]
#print mod137.Solution.singleNumber(sol137, quest)

#board = [["..9748..."],["7........"],[".2.1.9..."],["..7...24."],[".64.1.59."],[".98...3.."],["...8.3.2."],["........6"],["...2759.."]]
#board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
#board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
#sol36 = mod36.Solution()
#print mod36.Solution.isValidSudoku(sol36, board)
#print board

sol30 = mod30.Solution()
s = "barfoothefoofoobarman"
words = ["foo","bar","the","foo"]
print s
print words
print mod30.Solution.findSubstring(sol30, s, words)

"""
print board2[0]
print board2[1]
print board2[2]
print board2[3]
print board2[4]
print board2[5]
print board2[6]
print board2[7]
print board2[8]
"""