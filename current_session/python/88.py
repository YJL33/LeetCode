'''
88
'''
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c1, c2 = 0, 0
        if n == 0: return
        tmp = []
        while c1 < m and c2 < n:
            if nums1[c1] <= nums2[c2]:
                tmp.append(nums1[c1])
                c1 += 1
            else:
                tmp.append(nums2[c2])
                c2 += 1
        
        while c2 == n and c1 < m:
            tmp.append(nums1[c1])
            c1 += 1
        while c1 == m and c2 < n:
            tmp.append(nums2[c2])
            c2 += 1
        # print(tmp, nums1)
        for i in range(m+n):
            nums1[i] = tmp[i]
        return
