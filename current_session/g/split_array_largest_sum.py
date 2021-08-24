# minimize the largest sum when splitting the array into m parts
# try all m and all subA
# dp[m][i] is the solution of A[:i+1]

from typing import List
class Solution:
    def splitArray(self,A:List[int], M:int)->int:
        if M == len(A): return max(A)
        # use binary search to find the minimal largest sum

        l, r = max(A), sum(A)
        while l<r:
            mid = (r+l)//2
            if self.isValid(mid, M, A):      # could be too big, find left side
                r = mid
            else:
                l = mid+1
        return l

    def isValid(self, upper, m, A):
        # see if we can use mid as upper limit and separate A into M parts
        subSum = 0
        validGroupsCnts = 0
        for a in A:
            subSum += a
            if subSum > upper:
                validGroupsCnts, subSum = validGroupsCnts+1, a
        validGroupsCnts += 1
        return m >= validGroupsCnts


print(Solution().splitArray([1,2,3,4,5], 2))