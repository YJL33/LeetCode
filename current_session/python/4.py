"""
see https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 == []:
            return self.findMedianSortedArrays(nums2, nums2)
        if nums2 == []:
            return self.findMedianSortedArrays(nums1, nums1)

        # maintain 2 cursors
        n = len(nums1)+len(nums2)
        if n%2:
            return self.getL((n+1)/2, nums1, nums2)
        else:
            return (self.getL(n/2, nums1, nums2) + self.getR(n/2, nums1, nums2))/2.0


    def getL(self, cnt, arr1, arr2):
        l1, l2 = 0, 0
        last = 0
        while cnt and (l1 < len(arr1) or l2 < len(arr2)):
            if l2 == len(arr2):
                last = arr1[l1]
                l1 += 1
            elif l1 == len(arr1):
                last = arr2[l2]
                l2 += 1
            elif arr1[l1] <= arr2[l2]:
                last = arr1[l1]
                l1 += 1
            else:
                last = arr2[l2]
                l2 += 1
            cnt -= 1
        return last

    def getR(self, cnt, arr1, arr2):
        r1, r2 = len(arr1)-1, len(arr2)-1
        last = 0
        while cnt and (r1 >= 0 or r2 >= 0):
            if r2 < 0:
                last = arr1[r1]
                r1 -= 1
            elif r1 < 0:
                last = arr2[r2]
                r2 -= 1
            elif arr1[r1] >= arr2[r2]:
                last = arr1[r1]
                r1 -= 1
            else:
                last = arr2[r2]
                r2 -= 1
            cnt -= 1
        return last

print Solution().findMedianSortedArrays([1,3], [2])
print Solution().findMedianSortedArrays([1,2], [3,4])
print Solution().findMedianSortedArrays([2,2,2], [2,2,2,2])