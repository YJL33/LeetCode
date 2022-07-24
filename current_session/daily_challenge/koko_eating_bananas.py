from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find minimum k s.t. koko can eat all bananas
        # piles length <= h
        # worst k: max(piles)
        # best k (possibly): 1
        
        def is_valid(x):
            cnt = 0
            for p in piles:
                cnt += p//x + (0 if p%x == 0 else 1)
                if cnt > h: return False
            return True

        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2
            if is_valid(m):     # find smaller m -> r = m
                r = m
            else:
                l = m+1
        
        return l