from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, A: List[int]) -> bool:
        A.sort()
        for a in A:
            if mass < a: return False
            mass += a
        return True