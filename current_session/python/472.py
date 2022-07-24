from functools import cache
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # thoughts
        # parse to prefix and suffix
        ws = set(words)

        @cache
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in ws and suffix in ws:
                    return True
                if prefix in ws and dfs(suffix):
                    return True
                if suffix in ws and dfs(prefix):
                    return True
            
            return False
        
        res = []
        for w in words:
            if dfs(w):
                res.append(w)
        return res