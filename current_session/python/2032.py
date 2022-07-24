from typing import List
import collections
# weekly contest 262
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        numDict = collections.defaultdict(int)
        res = []
        for num in [nums1, nums2, nums3]:
            for n in set(num):
                numDict[n] += 1
        for k, v in numDict.items():
            if v >= 2: res.append(k)
        return res