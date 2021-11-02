from typing import List
class Solution:
    def maximizeSweetness(self, A: List[int], k: int) -> int:
        # use binary search
        # l, r = min(A), sum(A)/(k+1)
        # time analysis: nlog(m)
        # where n is length of sweetness, m is span of guess
        if k == len(A)-1: return min(A)

        # given sweetness x, can u get a minimum toal sweetness >= x in O(n)?
        # simply use prefixSum, and once the sum is bigger than x, add a new partition
        # in the end, check the number of partitions (at most k partitions)
        # outcome:
        # cuts == k, cut is good, keep find bigger x
        # cuts > k: too many partitions, cut is fine (simply merge)=> keep find bigger x
        # cuts < k: too few partitions, x is too big => find smaller x
        def canHaveSweetnessAfterDivide(x):
            cuts, cur = 0, 0
            divs = []
            for a in A:
                cur += a
                if cur >= x:      # each partition should >= x
                    divs.append(cur)
                    cur, cuts = 0, cuts+1
            if cur != 0: divs.append(cur)
            return cuts, divs

        l, r = 1, int(sum(A)/(k+1))
        while l < r:
            m = (l+r+1)//2
            cuts, _ = canHaveSweetnessAfterDivide(m)
            # print('given x:', m, 'parts:', divs, 'cuts', cuts, 'k', k)
            
            if cuts == k:
                r = m-1
            elif cuts > k:
                # l = m+1
                l = m
            else:
                r = m-1

        c, d = canHaveSweetnessAfterDivide(r)
        # print(c, d)
        return r

# print(Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], 5), 'should be 6')
# print(Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], 8), 'should be 1')
# print(Solution().maximizeSweetness([1,2,2,1,2,2,1,2,2], 2), 'should be 5')
# print(Solution().maximizeSweetness([1,2,2,1,2,2,1,2,2], 2), 'should be 5')
# print(Solution().maximizeSweetness([52832,63820,96186,1623,88717],3), 'should be 52832')
print(Solution().maximizeSweetness([90670,55382,95298,95795,73204,41464,18675,30104,47442,55307],6), 'should be 55382')
