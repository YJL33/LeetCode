"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print "input: \n{}\n{}".format(nums1, nums2)
        def kth(nums1, nums2, k, s1, e1, s2, e2):
            print "now: {} {} {} {} {}".format(k, s1, e1, s2, e2)
            if s1 >= e1:
                return nums2[s2+k]
            if s2 >= e2:
                return nums1[s1+k]
            if k == 0:
                return min(nums1[s1], nums2[s2])
            
            m = (e1+s1)/2
            n = (e2+s2)/2
            
            if (m-s1)+(n-s2) < k:
                if nums1[m] < nums2[n]:
                    return kth(nums1, nums2, k-(m-s1)-1, m+1, e1, s2, e2)
                else:
                    return kth(nums1, nums2, k-(n-s2)-1, s1, e1, n+1, e2)
            else: # m+n >= k, m+n cover k+1 element so we can reduce larger half
                if nums1[m] < nums2[n]:
                    return kth(nums1, nums2, k, s1, e1, s2, n)
                else:
                    return kth(nums1, nums2, k, s1, m, s2, e2)
    
        m = len(nums1)
        n = len(nums2)
        length = m+n
        if length % 2 == 0:
            return (kth(nums1, nums2, length/2-1, 0, m, 0, n) + kth(nums1, nums2, length/2, 0, m, 0, n))/2.0
        return kth(nums1, nums2, length/2, 0, m, 0, n)