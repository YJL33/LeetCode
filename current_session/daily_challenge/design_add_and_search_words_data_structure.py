class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        # add a word
        # e.g. add a word "boy"
        # root
        #   \ 
        #   node_a {"b": node_b}
        #      \ 
        #     node_b {"o": node_c}
        #        \ 
        #       node_c {"y": node_d}
        #          \ 
        #         node_d {is_word = True}
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        return
    
    def search(self, word):
        # search word if exist
        return self.dfs(self.root, word)

    def dfs(self, node, word: str) -> bool:
        if not word:
            return node.is_word
        if word[0] == '.':
            for child in node.children.values():
                if self.dfs(child, word[1:]):
                    return True
            return False
        else:
            if word[0] not in node.children:
                return False
            else:
                return self.dfs(node.children[word[0]], word[1:])

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)
        return

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)