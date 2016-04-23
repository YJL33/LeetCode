"""
275 H-Index-2

What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:
1. Expected runtime complexity is in O(log n) and the input is sorted. => Use binary search

"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        """
        N = len(citations)
        if N == 1 and citations[0] >= 1: return 1
        if N == 1 and citations[0] == 0: return 0
        if N == 0: return 0
        citations.insert(0,0)
        for i in xrange(N+1):
            if i+1 > citations[-1-i]: return i
        """

        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            mid = (low + high) / 2
            if N - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return N - low
