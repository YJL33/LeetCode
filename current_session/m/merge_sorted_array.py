from typing import List
class Solution:
    def merge(self, nums1:List[int], m:int, nums2:List[int], n:int) -> None:
        # first move zeros
        x, y = len(nums1)-1, m-1
        while y >= 0:
            nums1[x], nums1[y] = nums1[y], nums1[x]
            x, y = x-1, y-1

        # merge
        i, j = x+1, 0
        cur = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums1[cur] = nums1[i]
                cur, i = cur+1, i+1
            else:
                nums1[cur] = nums2[j]
                cur, j = cur+1, j+1
        
        while i < len(nums1):
            nums1[cur] = nums1[i]
            cur, i = cur+1, i+1
            
        while j < len(nums2):
            nums1[cur] = nums2[j]
            cur, j = cur+1, j+1
        
        # return nums1
        return

print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))