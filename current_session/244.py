'''
244

Design a class which receives a list of words in the constructor,
and implements a method that takes two words w1 and w2,
and return the shortest distance between these two words in the list.

Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
import collections
class WordDistance:

    def __init__(self, words: List[str]):
        self.wd = collections.defaultdict(list)
        for i in range(len(words)):
            self.wd[words[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1s, w2s = self.wd[word1], self.wd[word2]
        minDist = len(self.wd)
        for a in w1s:
            for b in w2s:
                minDist = min(minDist, abs(a-b))
        return minDist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)