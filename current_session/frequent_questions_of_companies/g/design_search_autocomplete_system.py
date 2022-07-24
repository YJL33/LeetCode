import collections
from typing import List
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isSentence = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, sentence: str) -> None:
        node = self.root
        for c in sentence:
            node = node.children[c]
        node.isSentence = True
        return

    def search(self, sentence: str) -> List[str]:
        node = self.root
        for c in sentence:
            if c not in node.children: return []
            node = node.children[c]

        # from here, return all possible sentences
        return self._dfs(node)
    
    def _dfs(self, node) -> List[str]:
        res = []
        if node.isSentence: res.append("")
        for k, v in node.children.items():
            res += [k+x for x in self._dfs(v)]
        return res

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.freqDict = collections.defaultdict(int)
        for i in range(len(sentences)):
            s = sentences[i]
            self.freqDict[s] = -1*times[i]
            self.trie.insert(s)
        self.prevInput = ""

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.prevInput += c
            rec = [(self.freqDict[self.prevInput+a], self.prevInput+a) for a in self.trie.search(self.prevInput)]
            rec.sort()
            return [r[1] for r in rec[:3]]
        else:
            self.trie.insert(self.prevInput)
            self.freqDict[self.prevInput] -= 1
            self.prevInput = ""
            return []
        
# Your AutocompleteSystem object will be instantiated and called as such:
obj = AutocompleteSystem(["i love you"],[5])
# obj = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
param_1 = obj.input("i")