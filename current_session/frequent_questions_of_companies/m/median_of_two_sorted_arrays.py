from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = len(nums1) + len(nums2)

        if L%2:
            return self.helper(nums1, nums2, L//2)
        else:
            return 0.5*(self.helper(nums1, nums2, L//2), self.helper(nums1, nums2, (L//2)-1))
    
    # find kth number in a sorted array
    def helper(self, A, B, k):
        if not B:
            return A[k]
        if not A:
            return B[k]
        
        a, b = len(A)//2, len(B)//2
        if a+b < k:                     # median at the right half
            if A[a] > B[b]:             # remove left side of B
                return self.helper(A, B[b+1:], k-b-1)
            else:                       # remove left side of A
                return self.helper(A[a+1:], B, k-a-1)
        else:                           # median at the left half
            if A[a] > B[b]:             # remove right half of A
                return self.helper(A[:a], B, k)
            else:                       # remove right half of B
                return self.helper(A, B[:b], k)

