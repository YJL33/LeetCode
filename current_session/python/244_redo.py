"""
244
"""
from typing import List
import collections
import bisect
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wd = collections.defaultdict(list)
        for i in range(len(wordsDict)):
            w = wordsDict[i]
            self.wd[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        minDist = float('inf')
        for pos1 in self.wd[word1]:
            x = bisect.bisect_left(self.wd[word2], pos1)
            tmp = [minDist]
            if x != 0:
                tmp.append(pos1-self.wd[word2][x-1])
            if x != len(self.wd[word2]):
                tmp.append(self.wd[word2][x]-pos1)
            minDist = min(tmp)
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)