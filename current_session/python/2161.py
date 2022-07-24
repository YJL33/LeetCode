from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p, l, r = [], [], []
        for n in nums:
            if n == pivot:
                p.append(n)
            elif n < pivot:
                l.append(n)
            else:
                r.append(n)
        return l+p+r