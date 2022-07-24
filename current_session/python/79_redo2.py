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
        
        # instead of modify the board, we use visited to track the path
        # (we can also use a 2D array to store visited)
        def dfs(i, j, k, visited):
            if word[k] != board[i][j]:
                return False
            if k+1 == len(word):
                return True
            
            visited.add((i,j))
            for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=a<H and 0<=b<W and (a,b) not in visited:
                    if dfs(a,b,k+1,visited): return True
            visited.remove((i,j))
            return False
        
        for i in range(H):
            for j in range(W):
                if dfs(i, j, 0, set((i,j))):
                    return True
        
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(Solution().exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],"aaaaaaaaaaaaa"))
print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))
