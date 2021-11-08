from typing import List
import collections
class Solution:
    def findNumOfValidWords_TLE(self, words: List[str], puzzles: List[str]) -> List[int]:
        # convert all word and puzzle into a set
        # phase 1: check whether the initial letter is included or not, time complexity O(m+n)
        # we can use space O(mn) to save some time on phase 2
        # phase 2: check whether w is a subset of p for each w and p, time complexity O(mn)
        # TLE

        W, P = [], []
        for w in words: W.append(set(w))
        for p in puzzles: P.append(set(p))

        checkFirst = [[-1 for _ in W] for _ in P]       # checkFirst[i][j]: check whether initial letter of P[i] is in W[j]
        for i in range(len(puzzles)):
            for j in range(len(W)):
                checkFirst[i][j] =  0 if puzzles[i][0] not in W[j] else 1
        
        res = []
        for i in range(len(P)):
            cnt = 0
            for j in range(len(words)):
                if checkFirst[i][j] == 0: continue
                if all([c in P[i] for c in words[j]]): cnt += 1
            res.append(cnt)
        
        return res

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # use bit mask
        # if set(w1) == set(w2) then we simply count twice
        maskDict = collections.defaultdict(int)
        for w in words:
            m = self.getBitMask(w)
            maskDict[m] += 1
        
        res = []
        for p in puzzles:
            first = ord(p[0]) - ord('a')
            puzzleMask = self.getBitMask(p)
            originalMask = puzzleMask
            cnt = 0
            # don't try each word's bitmask
            # instead, generate the permutation of puzzleMask
            while True:
                if puzzleMask >> first & 1:
                    cnt += maskDict[puzzleMask]
                if puzzleMask == 0:
                    break
                puzzleMask = (puzzleMask-1)&originalMask
            res.append(cnt)
        
        return res
    
    def getBitMask(self, w):
        mask = 0
        for c in w:
            mask |= 1 << ord(c)-ord('a')
        return mask


print(Solution().findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
print(Solution().findNumOfValidWords(words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]))