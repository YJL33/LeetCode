"""
179
"""
from functools import cmp_to_key
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        A = [str(x) for x in nums]
        A.sort(key=cmp_to_key(lambda x, y: -1 if x+y>y+x else y+x>x+y))
        return ''.join(A).lstrip('0') or '0'

print(Solution().largestNumber([10,2]))