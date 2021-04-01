"""
593
"""
from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # find the center
        # and check the vector
        points = [p1, p2, p3, p4]
        if len(set([(p1[0], p1[1]), (p2[0], p2[1]), (p3[0], p3[1]), (p4[0], p4[1])])) < 4: return False

        c = [1.0*sum([p[0] for p in points])/4, 1.0*sum([p[1] for p in points])/4]
        v = [p1[0]-c[0], p1[1]-c[1]]
        if [c[0]-v[1], c[1]+v[0]] not in points: return False
        if [c[0]+v[1], c[1]-v[0]] not in points: return False
        if [c[0]-v[0], c[1]-v[1]] not in points: return False
        return True

# true cases
print(Solution().validSquare([0,0],[1,1],[1,0],[0,1]))
print(Solution().validSquare([1134,-2539],[492,-1255],[-792,-1897],[-150,-3181]))
