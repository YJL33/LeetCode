#implement Trie
class TrieNode:
    def __init__(self):
        self.dct = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.dct:
                node.dct[c] = TrieNode()
            node = node.dct[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node, word)
    
    def dfs(self, node, word):
        if not word:
            return node.isWord
        if word[0] == '.':
            for child in node.dct.values():
                if self.dfs(child, word[1:]):
                    return True
            return False
        else:
            if word[0] not in node.dct:
                return False
            else:
                return self.dfs(node.dct[word[0]], word[1:])

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)