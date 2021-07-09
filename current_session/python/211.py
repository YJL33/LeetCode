"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""
import collections
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key: len of word, value: list of words
        self.wd = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.wd[len(word)].append(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.wd: return False
        words = self.wd[len(word)]
        for w in words:
            if self.check(w, word):
                return True
        return False
    
    def check(self, w, word):
        for i in range(len(word)):
            c1, c2 = w[i], word[i]
            if c2 != '.' and c1 != c2:
                return False
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)