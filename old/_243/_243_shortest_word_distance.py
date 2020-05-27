"""
243. Shortest Word Distance

    Total Accepted: 17733
    Total Submissions: 35906
    Difficulty: Easy

Given a list of words and two words word1 and word2,
return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2,
and word1 and word2 are both in the list.
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        worddct = {}
        for i in xrange(len(words)):
            w = words[i]
            if w in worddct:
                worddct[w] += i,
            else:
                worddct[w] = [i]

        mindist = len(words)
        for i in worddct[word1]:
            for j in worddct[word2]:
                mindist = min(mindist, abs(i-j))

        return mindist

    def shortestDistance(self, words, word1, word2):
        mindist = len(words)
        w1, w2, find, prev = -1, -1, 0, -1
        for i in xrange(len(words)):
            if words[i] == word1:
                w1, find = i, find+1
            elif words[i] == word2:
                w2, find = i, find+1
            if w1 != -1 and w2 != -1 and find != prev:
                mindist = min(mindist, abs(w1-w2))
                prev = find
        return mindist

