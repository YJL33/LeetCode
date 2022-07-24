
# see more at: https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/935/

import timeit
import bisect
class BS(object):
    def bs_finder(self, A, tgt):
        # all elements have to be unique
        l, r, m = 0, len(A)-1, 0
        while l <= r:                   # termination criteria l == r
            m = (r+l)//2
            if A[m] == tgt:             # directly return m
                return m
            elif A[m] > tgt:            # avoid repeatly handling m
                r = m-1
            else:
                l = m+1
        # assert(l == bisect.bisect_left(A, tgt))    
        return -1                       # no need post-processing

    def bs_left(self, A, tgt):
        # we wanna find max m s.t. A[m] <= tgt
        l, r, m = 0, len(A), 0
        while l < r:
            m = (r+l)//2
            if A[m] >= tgt:
                r = m
            else:
                l = m+1
        assert(l == bisect.bisect_left(A, tgt))         # binary search index left
        return l

    def bs_right(self, A, tgt):
        l, r, m = 0, len(A), 0
        while l < r:
            m = (r+l)//2
            if A[m] > tgt:
                r = m
            else:
                l = m+1
        assert(l == bisect.bisect_right(A, tgt))        # binary search index right
        return l

    # while finding the last element <= target
    def bs_lee(self, A, tgt):
        l, r, m = -1, len(A)-1, 0
        while l < r:
            m = (r+l+1)//2                              # add +1 due to l = m
            if A[m] > tgt:
                r = m-1
            else:
                l = m
        assert(l == -1 or (A[l]<=tgt and (l+1 == len(A) or A[l+1]>tgt)))
        return l

    # while finding the last element < target
    def bs_lee2(self, A, tgt):
        l, r, m = -1, len(A)-1, 0
        while l < r:
            m = (r+l+1)//2                              # add +1 due to l = m
            if A[m] >= tgt:
                r = m-1
            else:
                l = m
        assert(l == -1 or (A[l]<tgt and (l+1 == len(A) or A[l+1]>=tgt)))
        return l

print('bs finder ---')

print('given [0,2,4,6,8,10,12]-1:', BS().bs_finder([0,2,4,6,8,10,12],-1))
print('given [0,2,4,6,8,10,12] 0:', BS().bs_finder([0,2,4,6,8,10,12],0))
print('given [0,2,4,6,8,10,12] 1:', BS().bs_finder([0,2,4,6,8,10,12],1))
print('given [0,2,4,6,8,10,12] 2:', BS().bs_finder([0,2,4,6,8,10,12],2))
print('given [0,2,4,6,8,10,12] 3:', BS().bs_finder([0,2,4,6,8,10,12],3))
print('given [0,2,4,6,8,10,12] 4:', BS().bs_finder([0,2,4,6,8,10,12],4))
print('given [0,2,4,6,8,10,12] 5:', BS().bs_finder([0,2,4,6,8,10,12],5))

print('---')

print('given [0,2,2,2,2,2,2] -1:',BS().bs_finder([0,2,2,2,2,2,2],-1))
print('given [0,2,2,2,2,2,2] 0:', BS().bs_finder([0,2,2,2,2,2,2],0))
print('given [0,2,2,2,2,2,2] 1:', BS().bs_finder([0,2,2,2,2,2,2],1))
print('given [0,2,2,2,2,2,2] 2:', BS().bs_finder([0,2,2,2,2,2,2],2))
print('given [0,2,2,2,2,2,2] 3:', BS().bs_finder([0,2,2,2,2,2,2],3))
print('given [0,2,2,2,2,2,2] 4:', BS().bs_finder([0,2,2,2,2,2,2],4))
print('given [0,2,2,2,2,2,2] 5:', BS().bs_finder([0,2,2,2,2,2,2],5))

print('bs left ---')

print('given [0,2,4,6,8,10,12]-1:', BS().bs_left([0,2,4,6,8,10,12],-1))
print('given [0,2,4,6,8,10,12] 0:', BS().bs_left([0,2,4,6,8,10,12],0))
print('given [0,2,4,6,8,10,12] 1:', BS().bs_left([0,2,4,6,8,10,12],1))
print('given [0,2,4,6,8,10,12] 2:', BS().bs_left([0,2,4,6,8,10,12],2))
print('given [0,2,4,6,8,10,12] 3:', BS().bs_left([0,2,4,6,8,10,12],3))
print('given [0,2,4,6,8,10,12] 4:', BS().bs_left([0,2,4,6,8,10,12],4))
print('given [0,2,4,6,8,10,12] 5:', BS().bs_left([0,2,4,6,8,10,12],5))

print('---')

print('given [0,2,2,2,2,2,2] -1:',BS().bs_left([0,2,2,2,2,2,2],-1))
print('given [0,2,2,2,2,2,2] 0:', BS().bs_left([0,2,2,2,2,2,2],0))
print('given [0,2,2,2,2,2,2] 1:', BS().bs_left([0,2,2,2,2,2,2],1))
print('given [0,2,2,2,2,2,2] 2:', BS().bs_left([0,2,2,2,2,2,2],2))
print('given [0,2,2,2,2,2,2] 3:', BS().bs_left([0,2,2,2,2,2,2],3))
print('given [0,2,2,2,2,2,2] 4:', BS().bs_left([0,2,2,2,2,2,2],4))
print('given [0,2,2,2,2,2,2] 5:', BS().bs_left([0,2,2,2,2,2,2],5))

print('bs right ---')

print('given [0,2,4,6,8,10,12]-1:', BS().bs_right([0,2,4,6,8,10,12],-1))
print('given [0,2,4,6,8,10,12] 0:', BS().bs_right([0,2,4,6,8,10,12],0))
print('given [0,2,4,6,8,10,12] 1:', BS().bs_right([0,2,4,6,8,10,12],1))
print('given [0,2,4,6,8,10,12] 2:', BS().bs_right([0,2,4,6,8,10,12],2))
print('given [0,2,4,6,8,10,12] 3:', BS().bs_right([0,2,4,6,8,10,12],3))
print('given [0,2,4,6,8,10,12] 4:', BS().bs_right([0,2,4,6,8,10,12],4))
print('given [0,2,4,6,8,10,12] 5:', BS().bs_right([0,2,4,6,8,10,12],5))

print('---')

print('given [0,2,2,2,2,2,2] -1:', BS().bs_right([0,2,2,2,2,2,2],-1))
print('given [0,2,2,2,2,2,2] 0:', BS().bs_right([0,2,2,2,2,2,2],0))
print('given [0,2,2,2,2,2,2] 1:', BS().bs_right([0,2,2,2,2,2,2],1))
print('given [0,2,2,2,2,2,2] 2:', BS().bs_right([0,2,2,2,2,2,2],2))
print('given [0,2,2,2,2,2,2] 3:', BS().bs_right([0,2,2,2,2,2,2],3))
print('given [0,2,2,2,2,2,2] 4:', BS().bs_right([0,2,2,2,2,2,2],4))
print('given [0,2,2,2,2,2,2] 5:', BS().bs_right([0,2,2,2,2,2,2],5))

print('bs lee ---')

print('given [0,2,4,6,8,10,12]-1:', BS().bs_lee([0,2,4,6,8,10,12],-1))
print('given [0,2,4,6,8,10,12] 0:', BS().bs_lee([0,2,4,6,8,10,12],0))
print('given [0,2,4,6,8,10,12] 1:', BS().bs_lee([0,2,4,6,8,10,12],1))
print('given [0,2,4,6,8,10,12] 2:', BS().bs_lee([0,2,4,6,8,10,12],2))
print('given [0,2,4,6,8,10,12] 3:', BS().bs_lee([0,2,4,6,8,10,12],3))
print('given [0,2,4,6,8,10,12] 4:', BS().bs_lee([0,2,4,6,8,10,12],4))
print('given [0,2,4,6,8,10,12] 5:', BS().bs_lee([0,2,4,6,8,10,12],5))

print('---')

print('given [0,2,2,2,2,2,2] -1:',BS().bs_lee([0,2,2,2,2,2,2],-1))
print('given [0,2,2,2,2,2,2] 0:', BS().bs_lee([0,2,2,2,2,2,2],0))
print('given [0,2,2,2,2,2,2] 1:', BS().bs_lee([0,2,2,2,2,2,2],1))
print('given [0,2,2,2,2,2,2] 2:', BS().bs_lee([0,2,2,2,2,2,2],2))
print('given [0,2,2,2,2,2,2] 3:', BS().bs_lee([0,2,2,2,2,2,2],3))
print('given [0,2,2,2,2,2,2] 4:', BS().bs_lee([0,2,2,2,2,2,2],4))
print('given [0,2,2,2,2,2,2] 5:', BS().bs_lee([0,2,2,2,2,2,2],5))


print('bs lee 2---')

print('given [0,2,4,6,8,10,12]-1:', BS().bs_lee2([0,2,4,6,8,10,12],-1))
print('given [0,2,4,6,8,10,12] 0:', BS().bs_lee2([0,2,4,6,8,10,12],0))
print('given [0,2,4,6,8,10,12] 1:', BS().bs_lee2([0,2,4,6,8,10,12],1))
print('given [0,2,4,6,8,10,12] 2:', BS().bs_lee2([0,2,4,6,8,10,12],2))
print('given [0,2,4,6,8,10,12] 3:', BS().bs_lee2([0,2,4,6,8,10,12],3))
print('given [0,2,4,6,8,10,12] 4:', BS().bs_lee2([0,2,4,6,8,10,12],4))
print('given [0,2,4,6,8,10,12] 5:', BS().bs_lee2([0,2,4,6,8,10,12],5))

print('---')

print('given [0,2,2,2,2,2,2] -1:',BS().bs_lee2([0,2,2,2,2,2,2],-1))
print('given [0,2,2,2,2,2,2] 0:', BS().bs_lee2([0,2,2,2,2,2,2],0))
print('given [0,2,2,2,2,2,2] 1:', BS().bs_lee2([0,2,2,2,2,2,2],1))
print('given [0,2,2,2,2,2,2] 2:', BS().bs_lee2([0,2,2,2,2,2,2],2))
print('given [0,2,2,2,2,2,2] 3:', BS().bs_lee2([0,2,2,2,2,2,2],3))
print('given [0,2,2,2,2,2,2] 4:', BS().bs_lee2([0,2,2,2,2,2,2],4))
print('given [0,2,2,2,2,2,2] 5:', BS().bs_lee2([0,2,2,2,2,2,2],5))