"""
79
"""
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False

        H, W = len(board), len(board[0])

        # visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(i, j, c):
            if c == len(word): return True
            if board[i][j] == word[c]:
                board[i][j] = ''
                for a, b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=a<H and 0<=b<W and dfs(a,b,c+1):
                        return True
                board[i][j] = word[c]
            return False
        
        c = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, c): return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(Solution().exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],"aaaaaaaaaaaaa"))
print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))
