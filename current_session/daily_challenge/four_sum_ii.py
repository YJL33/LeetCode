from typing import List
import collections
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # naive approach
        # get all possible sums from n1 and n2 => x1, n3 and n4 => x2
        # then do 2 sum on x1 and x2
        # time complexity O(n^2)
        x1 = collections.defaultdict(int)
        x2 = collections.defaultdict(int)
        def helper(n1, n2, x):
            for a in n1:
                for b in n2:
                    x[a+b] += 1
            return
        helper(nums1, nums2, x1)
        helper(nums3, nums4, x2)

        cnt = 0
        for k1, v1 in x1.items():
            if -k1 in x2:
                cnt += v1*x2[-k1]
        return cnt