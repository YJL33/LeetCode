class Solution:
    def __init__(self):
        self.cnt = 0
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def msort(A):
            # merge sort body
            L = len(A)
            if L <= 1:                          # base case
                return A
            else:                               # recursive case
                return merger(msort(A[:int(L/2)]), msort(A[int(L/2):]))
        def merger(left, right):
            l, r = 0, 0                         # increase l and r iteratively
            while l < len(left) and r < len(right):
                if left[l] <= 2*right[r]:
                    l += 1
                else:
                    self.cnt += len(left)-l     # COUNT here
                    r += 1
            
            res = []                            # merger
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res += left[i],
                    i += 1
                else:
                    res += right[j],
                    j += 1
            
            while i != len(left):
                res += left[i],
                i += 1
            while j != len(right):
                res += right[j],
                j += 1
            
            return res

        msort(nums)
        return self.cnt