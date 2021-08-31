"""
trie+dfs+backtrack
"""
from typing import List
class Node:
    def __init__(self,val=None,endhere=False):
        '''
        count: count how many times a charater is used. When count reachs zero, we can't use that trie branch anymore
        endhere: mark the completion of a word
        '''
        self.val = val
        self.child = {}
        self.count = 0
        self.endhere = endhere


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        1. Build a trie from starting words
        2. Mark end here to mark word
        3. Backtracking from every position in board
        4. Keep track of current visited position by a set

        '''
        ROWS = len(board)
        COLS = len(board[0])
        # Build Trie
        root = Node()
        for word in words:
            cur = root
            cur.count +=1
        
            for char in word:
                if char not in cur.child:
                    cur.child[char]=Node(val=char)
                cur = cur.child[char]
                cur.count +=1
            
            cur.endhere = True


        def backtrack(r,c,visited,node,board,candidate):
            '''
            r: the row in the board
            c: the column in the board
            visited: a set of tuples (r,c) that were visited in the current round
            node: the parent node of this function call
            board: the given charater board
            candidate: a list of characters that are under considering
            
            '''
             
            char = board[r][c]
            if char in node.child:
                node = node.child[char]
                # if the Trie branch is used up, do not consider them in further call
                if node.count == 0:
                    return
                
                visited.add((r,c))
                candidate.append(char)
                if node.endhere == True:
                    # Found a target string, chop the tree branch that leads to this word
                    res.add("".join(candidate))
                    cur = root
                    cur.count -=1
                    for ele in candidate:
                        cur = cur.child[ele]
                        cur.count -=1
                    
                # check 4 potential adjacent location for next backtracking call
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_row = r+dr
                    new_col = c+dc 
                    if (new_row,new_col) not in visited and 0 <= new_row < ROWS \
                    and 0 <= new_col < COLS:
                        backtrack(new_row,new_col,visited,node,board,candidate)
                #pop out candidate at the same level as they were added in
                visited.remove((r,c))
                candidate.pop()



        
        res = set()
        # start a new backtracking call at every position of the board
        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                candidate = []
                backtrack(i,j,visited,root,board,candidate)

        return list(res)

    

t = Trie()
t.insert("abc")
t.insert("def")
print(t.search("abc"))
print(t.search("def"))
print(t.search("defgh"))
print(t.search("ab"))