"""
243
"""
from typing import List
import collections
class Solution:
    # O(n)
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pw, pi = None, None
        minDist = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] in (word1, word2):
                if pw and wordsDict[i] != pw:
                    minDist = min(minDist, i-pi)
                pw, pi = wordsDict[i], i
        return minDist