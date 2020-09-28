class Solution(object):
    def findMedianSortedArrays(self, P, Q):
        l = len(P)+len(Q)
        print "l:", l
        if l%2:
            return self.finder(l//2, P, Q)
        else:
            return (self.finder(l//2, P, Q) + self.finder((l//2)-1, P, Q)) / 2.0

    def finder(self, k, P, Q):
        # count smaller elements leveraging bisect
        print k, P, Q
        if not P:
            return Q[k]
        if not Q:
            return P[k]
        p, q = len(P)/2, len(Q)/2

        if p+q < k:     # median is in right half
            if P[p] > Q[q]:
                return self.finder(k-q-1, P, Q[q+1:])     # remove Q's left
            else:
                return self.finder(k-p-1, P[p+1:], Q)
        else:           # median is in left half
            if P[p] > Q[q]:
                return self.finder(k, P[:p], Q) # remove P's right
            else:
                return self.finder(k, P, Q[:q])

print(Solution().findMedianSortedArrays([0,0],[0,0]))
print(Solution().findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1]))
print(Solution().findMedianSortedArrays([1,3],[2]))
print(Solution().findMedianSortedArrays([1,2,3,4,5,6,7,8,9],[10]))