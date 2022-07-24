from typing import List
import collections
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # clarification
        # very similar to #954
        if sum(changed)%3 or len(changed)%2: return []
        cnt = collections.Counter(changed)
        keys = [k for k in cnt.keys()]
        keys.sort()
        ans = []
        for k in keys:
            if cnt[k] > cnt[2*k]:
                return []
            if k != 0:
                ans += [k]*cnt[k]
            else:
                ans += [k]*(cnt[k]//2)
            cnt[2*k] -= cnt[k]
            
        return ans
        