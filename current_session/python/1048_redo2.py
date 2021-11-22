from typing import List
import collections
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # first put all words into dict
        # key: length, value: list of words
        # start to search from shortest words
        # tip: find from longest to shortest, instead of opposite
        ld = collections.defaultdict(set)
        minLen = float('inf')
        for w in words:
            ld[len(w)].add(w)
            minLen = min(minLen, len(w))
        
        self.maxCnt = 0
        self.visited = collections.defaultdict(int)

        def dfs(w, cnt):
            self.maxCnt = max(self.maxCnt, cnt)
            if w in self.visited and self.visited[w] >= cnt: return
            self.visited[w] = cnt
            # try to insert a character in the gap
            for i in range(len(w)):
                newWord = w[:i] + w[i+1:]
                if newWord != "" and newWord in ld[len(w)-1]:
                    dfs(newWord, cnt+1)
            return

        # try all words as beginning
        for w in words:
            dfs(w, 1)
        
        return self.maxCnt

print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(Solution().longestStrChain(["abcd","dbqca"]))
print(Solution().longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]), 'should be 7')