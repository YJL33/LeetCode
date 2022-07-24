from typing import List
class Solution:
    def maximizeSweetness(self, A: List[int], k: int) -> int:
        # use binary search
        # check whether we can split the chocolate into k parts, and min sweetness >= guess
        # the result(guess) and k should have the following relationship:
        # k == 1: res = sum(A)
        # k == len(A): res = min(A)
        # decrease guess -> increase k
        # initial guess: l, r = min(A), sum(A)
        
        if k == len(A)-1: return min(A)
        
        def islegit(x):
            cnt, local_sum = 0, 0
            for a in A:
                local_sum += a
                if local_sum >= x:
                    cnt += 1
                    local_sum = 0
            return cnt
        
        # binary search
        # say m is legit (can split chocolate into (at least) k parts, and min sweetness >= m)
        # we want to find bigger m
        l, r = min(A), sum(A)
        while l < r:
            m = (l+r+1)//2
            if islegit(m) >= k+1:
                l = m
            else:
                r = m-1
        
        return l