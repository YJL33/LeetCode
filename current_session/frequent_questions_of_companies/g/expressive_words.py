from typing import List
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        cnt = 0
        set_of_s = set(s)

        def can_stretch(w):
            for c in w:
                if c not in set_of_s:
                    return 0
            i, j = 0, 0
            while i < len(s) and j < len(w):
                a, b = s[i], w[j]
                if a != b: return 0
                cntA, cntB = 1, 1
                while i+1 < len(s) and s[i+1] == a:
                    i += 1
                    cntA += 1
                while j+1 < len(w) and w[j+1] == b:
                    j += 1
                    cntB += 1
                if cntA == cntB or (cntA >= 3 and cntA > cntB):
                    i, j = i+1, j+1
                else:
                    break
            return (i == len(s) and j == len(w))

        for w in words:
            if can_stretch(w):
                cnt += 1
                # print('w', w)
        return cnt