from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
# use bfs
        ws = set(wordList)
        dq = collections.deque([(beginWord,1)])
        if endWord not in ws: return 0
        while len(dq) > 0:
            w, cnt = dq.popleft()
            if w == endWord:
                return cnt
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = w[:i]+c+w[i+1:]
                        if tmp in ws:
                            dq.append((tmp,cnt+1))
                            ws.remove(tmp)      # critical: we always visit each word in the earliest possible time
        return 0