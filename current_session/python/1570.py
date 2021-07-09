"""
1570
"""
import collections
class SparseVector:
    # Get TLE if use bitwise operation...
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nd = {}
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != 0:
                self.nd[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for k, v in self.nd.items():
            if k in vec.nd.keys():
                res += v*vec.nd[k]
        return res

    
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)