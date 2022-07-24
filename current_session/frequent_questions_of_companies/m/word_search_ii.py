from typing import List
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.cnt = 0
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.cnt = float('inf')
    
    def insert(self, s):
        node = self.root
        for c in s:
            node = node.children[c]
            node.cnt += 1
        node.isEnd = True
        return
    
    def remove(self, s):
        node = self.root
        for c in s:
            node = node.children[c]
            node.cnt -= 1
        node.isEnd = False
        return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # print('board:', board)
        H, W = len(board), len(board[0])
        self.res = set()

        # 1. add all words into Trie
        t = Trie()
        for w in words:
            t.insert(w)

        # DFS
        def dfs(i, j, node, prefix=""):
            # add word first
            if node.isEnd:
                self.res.add(prefix)
                t.remove(prefix)

            # termination
            if i == -1 or i == H or j == -1 or j == W: return
            c = board[i][j]
            if c not in node.children: return
            if node.children[c].cnt == 0: return

            # check all neighbors
            board[i][j] = "#"
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(i+di,j+dj,node.children[c],prefix+c)
            board[i][j] = c
            return

        # 2. for each i, j on the board, dfs on the trie
        for row in range(H):
            for col in range(W):
                node = t.root
                dfs(row, col, node)
        
        return [r for r in self.res]

print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
print(Solution().findWords([["a"]],["a"]))
print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","oathk","oathf","oathfi","oathfii","oathi","oathii","oate","eat"]))