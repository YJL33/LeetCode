# edge case: if endword is not in wordList
# from starting word, check if next word exist or not
# use BFS and a deque
from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        queue = collections.deque([[beginWord, 1]])
        while queue:
            w, l = queue.popleft()
            if w == endWord:
                return l
            for c in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(w)):
                    nextWord = w[:i] + c + w[i+1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append([nextWord, l+1])
        return 0


print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("hit","cog",["hot","cog","dot","dog","hit","lot","log"]))
print(Solution().ladderLength("hit","hit",["hot","cog","dot","dog","hit","lot","log"]))