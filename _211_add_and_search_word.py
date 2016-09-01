"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string,
containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z. 
"""
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dct = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            if len(word) not in self.dct:
                self.dct[len(word)] = [word]
            else:
                self.dct[len(word)] += word,

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if len(word) not in self.dct:
            return False
        if '.' not in word:
            return word in self.dct[len(word)]
        for val in self.dct[len(word)]:
            for i, ch in enumerate(word):
                if ch != val[i] and ch != '.':
                    break
            else:
                return True
        return False