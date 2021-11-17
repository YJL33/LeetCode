class Solution:
    def findKthNumber(self, m, n, k):
        # use binary search to find the kth smallest number
        # we should have a method that calculates the number that smaller than k
        # e.g. (m, n, k) = (3,3,4)
        # if we guess 2 -> we have 3 numbers smaller or equal to 2 (too few)
        # if we guess 3 -> we have 5 numbers smaller or equal to 3
        # if we guess 4 -> we have 6 numbers smaller or equal to 4 (too many)
        # return 3
        l, r = 1, m*n
        def count(x,m,n):
            # count the numbers that smaller than x in mult. table
            # count row by row
            count = 0
            for i in range(1, m+1):
                count += min(n, x//i)
            return count
        while l < r:
            mid = (l+r)//2
            if count(mid,m,n) < k:
                l = mid+1
            else:
                r = mid
        return r

print(Solution().findKthNumber(9895,28405,100787757))