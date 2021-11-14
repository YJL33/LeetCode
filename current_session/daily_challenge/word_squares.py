# use dfs
# use each word as first row
# establish prefix dict
from typing import List
import collections
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # establish prefix dict
        self.pd = collections.defaultdict(list)
        for w in words:
            for i in range(1,len(w)):
                self.pd[w[:i]].append(w)
        
        self.res = []
        # dfs
        def dfs(first, j, path=[]):
            # print('path:', path)
            if j == len(first):
                self.res.append([first]+path)
                return
            prefix = first[j]+''.join([x[j] for x in path])
            for w in self.pd[prefix]:
                tmp = [x for x in path]
                dfs(first, j+1, tmp+[w])
            return
        
        for w in words:
            dfs(w, 1)
        
        return self.res

print(Solution().wordSquares(["area","lead","wall","lady","ball"]))