# use a dict: key = word, value= list of index
# O(n) + O(a*logb), where a is number of w1, b is number of w2

# simply scan the whole array
# store the previous i, where w[i] in (w1, w2), update the minDist
# O(n)

from typing import List
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pw, pi = None, None
        minDist = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] in (word1, word2):
                if pw and wordsDict[i] != pw:
                    minDist = min(minDist, i-pi)
                pw, pi = wordsDict[i], i
        return minDist
