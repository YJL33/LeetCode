# intersection of 2 arrays
from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Dict = collections.defaultdict(int)
        for n in nums2:
            nums2Dict[n] += 1

        ans = []
        for n in nums1:
            if n in nums2Dict and nums2Dict[n] > 0:
                nums2Dict[n] -= 1
                ans.append(n)
            if nums2Dict[n] == 0:
                del nums2Dict[n]
        return ans
            
print(Solution().intersect([1,2,2,1],[2,2]))
print(Solution().intersect([4,9,5],[9,4,9,8,4]))