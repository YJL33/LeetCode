"""
https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
"""
class Solution(object):
    # use BFS
    def findMedianSortedArrays2(self, P, Q):
        l = len(P)+len(Q)
        if l%2:
            return self.kth(l//2, P, Q)
        else:
            return (self.kth(l//2, P, Q) + self.kth((l//2)-1, P, Q)) / 2.0

    def kth(self, k, P, Q):
        # print k, P, Q
        if len(P) == 0:
            return Q[k]
        if len(Q) == 0:
            return P[k]

        p, q = len(P)/2, len(Q)/2
        # print p, q, P[p], Q[q]
        
        if p+q < k:                                 # median is in left half
            if P[p] > Q[q]:
                return self.kth(k-q-1, P, Q[q+1:])  # remove Q's right half
            else:
                return self.kth(k-p-1, P[p+1:], Q)  # remove P's right half
        else:                                       # median is in right half
            if P[p] > Q[q]:
                return self.kth(k, P[:p], Q)        # remove P's left half
            else:
                return self.kth(k, P, Q[:q])        # remove Q's right half

print(Solution().findMedianSortedArrays([0,0],[0,0]))
print(Solution().findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1]))
print(Solution().findMedianSortedArrays([1,3],[2]))
print(Solution().findMedianSortedArrays([1,2,3,4,5,6,7,8,9],[10]))