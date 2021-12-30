# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # use binary search
        # find in both side
        
        def find_peak_index(mt):
            l, r = 0, mt.length()-1
            while l < r:
                m = (l+r)//2
                nb_l, mid, nb_r = mt.get(m-1) if m!=0 else None, mt.get(m), mt.get(m+1) if m<r else None
                if (not nb_l or mid > nb_l) and (not nb_r or mid > nb_r): return m
                elif nb_r and (nb_r > mid):        # increasing, peak at the right side
                    l = m+1
                else:
                    r = m-1
            return l
        
        def finder(mt, tgt, pi, isReverse=False):
            l, r = pi if isReverse else 0, mt.length()-1 if isReverse else pi
            while l <= r:
                m = (l+r)//2
                if mt.get(m) == tgt: return m
                elif mt.get(m) > tgt:       # too close to peak
                    l, r = m+1 if isReverse else l, r if isReverse else m-1
                else:
                    l, r = l if isReverse else m+1, m-1 if isReverse else r
            return -1
        
        L = mountain_arr.length()
        head, tail = mountain_arr.get(0), mountain_arr.get(L-1)
        if target == head: return 0
        if target < head and target < tail: return -1           # too small, no need to search
            
        peakIndex = find_peak_index(mountain_arr)       
        peak = mountain_arr.get(peakIndex)
        if target > peak: return -1                             # too big, no need to search
        if target == peak: return peakIndex

        # find left side
        left = finder(mountain_arr, target, peakIndex)
        if left != -1: return left
        if target == tail: return L-1                           # no need to search in right side
        
        # find right side
        right = finder(mountain_arr, target, peakIndex, True)
        if right != -1: return right
        
        return -1
        