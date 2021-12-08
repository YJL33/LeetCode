import collections
from typing import List
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = collections.defaultdict(int)
        cnt2 = collections.defaultdict(int)
        for w in words1:
            cnt1[w] += 1
        
        for w in words2:
            cnt2[w] += 1
        
        ans = 0
        for k, v in cnt1.items():
            if v == 1 and cnt2[k] == 1:
                ans += 1
        
        return ans
                
        
        