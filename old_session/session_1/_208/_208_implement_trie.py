"""
 208. Implement Trie (Prefix Tree)

    Total Accepted: 57799
    Total Submissions: 226222
    Difficulty: Medium
    Contributors: Admin

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = False       # records whether here ends a word
        self.kids = {}          # records this node's kid

class Trie(object):

    def __init__(self):
        self.root = TrieNode()  # nothing but records some initials

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for i in word:
            if i not in cur.kids: cur.kids[i] = TrieNode()          # if not in its kids, add it
            cur = cur.kids[i]                                       # go down one level
        cur.word = True         # Here a word ends

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # Directly go down, if any non-existence => return False.
        cur = self.root
        for i in word:
            if i not in cur.kids: return False
            cur = cur.kids[i]
        return cur.word         # Return whether here ends a word or not

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # Directly go down, if any non-existence => return False
        cur = self.root
        for i in prefix:
            if i not in cur.kids: return False
            cur = cur.kids[i]
        return True             # if every char in the word exists => MUST True.
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")