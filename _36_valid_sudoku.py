"""
36 Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
class Solution(object):
    """ Solution for LEETCODE """
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict = {}
        # Check horizontally
        for row in board:
            for i in xrange(0, 9):
                if row[i] not in dict:
        			#print row[x]
                    dict[row[i]] = 1     # Record all unique elements
            if row.count(".") + len(set(row)) - 1 != 9:
        		#print "row err"
                return False
        # Check number of elements
        if len(dict) > 10:
        	#print "dict err"
            return False
        # Check vertically
        for j in xrange(0, 9):
            col = [row[j] for row in board]
            if col.count(".") + len(set(col)) - 1 != 9:
        		#print "col err"
        	    return False
        # Check local square
        for i in xrange(0, 7, 3):
            for j in xrange(0, 7, 3):
                sqre = [board[i + m][j + n] for m in xrange(3) for n in xrange(3)]
                if sqre.count(".") + len(set(sqre)) - 1 != 9:
        	    	#print "sqre err"
                    return False
        return True
        