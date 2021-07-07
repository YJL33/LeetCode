"""
347
"""
from typing import List
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        return [x[0] for x in cnt.most_common(k)]