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
        # use bfs
        wd = collections.defaultdict(int)
        wordSet = set(wordList)
        dq = collections.deque([(beginWord,1)])
        while len(dq) > 0:
            w, cnt = dq.pop()
            if w == endWord:
                return cnt
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nxt = w[:i]+c+w[i+1:]
                        if nxt in wordSet:
                            dq.appendleft((nxt,cnt+1))
                            wordSet.remove(nxt)
        return 0