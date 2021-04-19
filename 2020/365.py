"""
365
"""
import math
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or x + y >= z and z % math.gcd(x, y) == 0

# print(Solution().canMeasureWater(13,11,1))