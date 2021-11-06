from typing import List
class Solution:
    def singleNumber(self, A: List[int]) -> List[int]:
        seen = set()
        for a in A:
            if a not in seen:
                seen.add(a)
            else:
                seen.remove(a)
        return [x for x in seen]