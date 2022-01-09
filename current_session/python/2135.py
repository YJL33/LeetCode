from typing import List
import collections
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        wd = collections.defaultdict(set)
        def to_sig(word):
            tmp = [c for c in word]
            tmp.sort()
            return ''.join(tmp)

        for w in startWords:
            wd[len(w)].add(to_sig(w))
        
        cnt = 0
        for t in targetWords:
            l = len(t)-1
            for i in range(len(t)):
                tmp = t[:i]+t[i+1:]
                if to_sig(tmp) in wd[l]:
                    cnt += 1
                    break
        return cnt
