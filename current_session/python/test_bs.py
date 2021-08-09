import timeit
import bisect
class BS(object):
    # we wanna find max m s.t. L[m] <= tgt
    def bs(self, L, tgt):
        t = timeit.Timer()

        cd = [0,2,3,4,5,6,7,12]
        # print("L, tgt", L, tgt)

        l, r, m = 0, len(L)-1, 0
        cnt = 10

        while l < r and cnt > 0:
            m = (r+l)//2
            if L[m] >= tgt:
                r = m
            else:
                l = m+1
            # print(l, r, m)
            cnt -= 1
        # print("l, m, r",l, m, r)
        # print("t1:", t.timeit())

        # t2 = timeit.Timer()
        # i = bisect.bisect_left(L, tgt)
        # print("t2", t2.timeit())

        return l

print(BS().bs([0,2,4,6,8,10,12],0))
print(BS().bs([0,2,4,6,8,10,12],1))
print(BS().bs([0,2,4,6,8,10,12],2))
print(BS().bs([0,2,4,6,8,10,12],3))
print(BS().bs([0,2,4,6,8,10,12],4))
print(BS().bs([0,2,4,6,8,10,12],5))

print('---')

print(BS().bs([0,2,2,2,2,2,2],0))
print(BS().bs([0,2,2,2,2,2,2],1))
print(BS().bs([0,2,2,2,2,2,2],2))
print(BS().bs([0,2,2,2,2,2,2],3))
print(BS().bs([0,2,2,2,2,2,2],4))
print(BS().bs([0,2,2,2,2,2,2],5))