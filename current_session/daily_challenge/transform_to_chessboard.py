# https://leetcode.com/problems/transform-to-chessboard/discuss/440085/Python-detailed-explanation
# implement helper: verify the board is good or not
# count the number of swaps
from typing import List
import collections
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        if len(board) <= 1: return 0
        if not self.isValid(board): return -1
        n = len(board)
        rowdiff=sum(board[0][i]!=(i%2) for i in range(n))
        coldiff=sum(board[i][0]!=(i%2) for i in range(n))
        rowdiff=n-rowdiff if rowdiff%2!=0 or (n%2==0 and (n-rowdiff)<rowdiff) else rowdiff
        coldiff=n-coldiff if coldiff%2!=0 or (n%2==0 and (n-coldiff)<coldiff) else coldiff
        return (rowdiff+coldiff)//2
    
    def isValid(self, board):
        rows = [''.join(str(c) for c in r) for r in board]
        counter = collections.Counter(rows)
        keys = [k for k in counter.keys()]
        a, b = keys[0], keys[1]
        
        if len(keys) != 2: return False
        if abs(counter[a] - counter[b]) > 1: return False
        if abs(a.count('1') - a.count('0')) > 1: return False
        if any([a[i] == b[i] for i in range(len(a))]): return False

        return True