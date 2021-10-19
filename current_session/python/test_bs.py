
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

print('bs finder ---')

print(BS().bs_finder([0,2,4,6,8,10,12],0))
print(BS().bs_finder([0,2,4,6,8,10,12],1))
print(BS().bs_finder([0,2,4,6,8,10,12],2))
print(BS().bs_finder([0,2,4,6,8,10,12],3))
print(BS().bs_finder([0,2,4,6,8,10,12],4))
print(BS().bs_finder([0,2,4,6,8,10,12],5))

# print('---')

# print(BS().bs_finder([0,2,2,2,2,2,2],0))
# print(BS().bs_finder([0,2,2,2,2,2,2],1))
# print(BS().bs_finder([0,2,2,2,2,2,2],2))
# print(BS().bs_finder([0,2,2,2,2,2,2],3))
# print(BS().bs_finder([0,2,2,2,2,2,2],4))
# print(BS().bs_finder([0,2,2,2,2,2,2],5))

print('bs left ---')

print(BS().bs_left([0,2,4,6,8,10,12],0))
print(BS().bs_left([0,2,4,6,8,10,12],1))
print(BS().bs_left([0,2,4,6,8,10,12],2))
print(BS().bs_left([0,2,4,6,8,10,12],3))
print(BS().bs_left([0,2,4,6,8,10,12],4))
print(BS().bs_left([0,2,4,6,8,10,12],5))

# print('---')

# print(BS().bs_left([0,2,2,2,2,2,2],0))
# print(BS().bs_left([0,2,2,2,2,2,2],1))
# print(BS().bs_left([0,2,2,2,2,2,2],2))
# print(BS().bs_left([0,2,2,2,2,2,2],3))
# print(BS().bs_left([0,2,2,2,2,2,2],4))
# print(BS().bs_left([0,2,2,2,2,2,2],5))

print('bs right ---')

print(BS().bs_right([0,2,4,6,8,10,12],0))
print(BS().bs_right([0,2,4,6,8,10,12],1))
print(BS().bs_right([0,2,4,6,8,10,12],2))
print(BS().bs_right([0,2,4,6,8,10,12],3))
print(BS().bs_right([0,2,4,6,8,10,12],4))
print(BS().bs_right([0,2,4,6,8,10,12],5))

# print('---')

# print(BS().bs_right([0,2,2,2,2,2,2],0))
# print(BS().bs_right([0,2,2,2,2,2,2],1))
# print(BS().bs_right([0,2,2,2,2,2,2],2))
# print(BS().bs_right([0,2,2,2,2,2,2],3))
# print(BS().bs_right([0,2,2,2,2,2,2],4))
# print(BS().bs_right([0,2,2,2,2,2,2],5))