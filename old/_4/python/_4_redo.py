"""
 4. Median of Two Sorted Arrays

    Total Accepted: 143866
    Total Submissions: 685936
    Difficulty: Hard
    Contributors: Admin

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

        def kth(k, s1, s2, e1, e2):         # k is index of combined array
            # assert e1 >= s1 and e2 >= s2
            # print k, s1, s2, e1, e2
            if s1 >= e1:
                return nums2[s2+k]
            if s2 >= e2:
                return nums1[s1+k]
            if k == 0:
                return min(nums1[s1], nums2[s2])

            m1, m2 = (s1+e1)/2, (s2+e2)/2

            if m1-s1+m2-s2 < k:             # cut the part before median
                if nums1[m1] < nums2[m2]:   # cut nums1
                    return kth(k-(m1-s1)-1, m1+1, s2, e1, e2)
                else:                       # cut nums2
                    return kth(k-(m2-s2)-1, s1, m2+1, e1, e2)
            else:                           # cut the part after median
                if nums1[m1] > nums2[m2]:   # cut nums2
                    return kth(k, s1, s2, m1, e2)
                else:                       # cut nums1
                    return kth(k, s1, s2, e1, m2)
        
        m, n = len(nums1), len(nums2)
        if (m + n) % 2:
            return kth((m + n)/2, 0, 0, m, n)
        else:
            return 0.5*kth((m + n)/2, 0, 0, m, n) + 0.5*kth((m + n)/2-1, 0, 0, m, n)
        

def main():
    test1a = [1,3]
    test1b = [2]
    test2a = [1,2]
    test2b = [3,4,5,6,7]
    print test1a, test1b
    print Solution().findMedianSortedArrays(test1a, test1b)
    print test2a, test2b
    print Solution().findMedianSortedArrays(test2a, test2b)

if __name__ == "__main__":
    main()