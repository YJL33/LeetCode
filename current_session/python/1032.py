from typing import List
# simply implement a trie-like structure
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.children = {}          # key: children val, val: children node

class Trie:
    def __init__(self):
        self.head = TrieNode(0)
    
    def addWord(self, word):
        cur = self.head
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.addWord(w)
        self.actives = []           # nodes of active starting position, always have self.Trie
        self.actives += self.trie.head,

    def query(self, letter: str) -> bool:
        self.actives = [self.trie.head] + [p.children[letter] for p in self.actives if letter in p.children]
        return any([x.isEnd for x in self.actives])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)