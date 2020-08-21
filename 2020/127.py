"""
see https://leetcode.com/problems/word-ladder/
"""
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # use bfs and leverage deque

        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        queue = collections.deque([[beginWord, 1]])
        while queue:
            w, l = queue.popleft()
            if w == endWord:
                return l
            for i in range(len(w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = w[:i] + c + w[i+1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append([nextWord, l+1])
        return 0

print Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])