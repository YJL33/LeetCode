"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns True,
word = "SEE", -> returns True,
word = "ABCB", -> returns False.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False

        # seek through the board and apply helper.
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.helper(i,j,board,word): return True
        # if go after this line means finding nothing valid
        return False

    def helper(self, i, j, board, word):
        # For each grid, check whether it's valid or not.
        # if valid, go check next
        # else, restore the grid.
        if board[i][j] == word[0]:
            board[i][j] = ''
            h, w = len(board), len(board[0])
            coordinate = [(1,0),(-1,0),(0,1),(0,-1)]
            # check i, j's neighbor
            for c in coordinate:
                y, x= i+c[0], j+c[1]
                if y>=0 and y<h and x>=0 and x<w and self.helper(y,x,board,word[1:]):
                    return True
            # if go after this line means finding nothing valid
            board[i][j] = word[0]
            return False
        elif board[i][j] != word[0]:
            return False
