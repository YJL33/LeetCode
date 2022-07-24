from typing import List
import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.cnt = 0
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.root.cnt = float('inf')
    
    def insert(self, word):
        node = self.root
        for c in word:
            # node[c] = Node()
            node = node.children[c]
            node.cnt += 1
        node.is_end = True
        return
    
    def remove(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            node.cnt -= 1
        node.is_end = False
        return
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        H, W = len(board), len(board[0])
        # use Trie
        t = Trie()
        
        for w in words:
            t.insert(w)
        
        def dfs(i, j, node, prefix=""):
            if node.is_end:
                self.res.append(prefix)
                t.remove(prefix)

            # check boundary
            if i < 0 or i == H or j < 0 or j == W: return
            # termination
            c = board[i][j]
            if c not in node.children: return
            if node.children[c].cnt == 0: return
            
            board[i][j] = "#"
            for a, b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                dfs(a, b, node.children[c], prefix+c)
            board[i][j] = c
            return

        # dfs the board
        self.res = []
        for i in range(H):
            for j in range(W):
                node = t.root
                dfs(i, j, node)
        
        return self.res

print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
print(Solution().findWords([["a"]],["a"]))
print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","oathk","oathf","oathfi","oathfii","oathi","oathii","oate","eat"]))