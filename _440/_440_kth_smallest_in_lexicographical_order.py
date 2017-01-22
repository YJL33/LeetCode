"""
440. K-th Smallest in Lexicographical Order

    User Tried: 1
    Total Submissions: 1
    Difficulty: Medium

Given integers n and k,
find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 <= k <= n <= 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
so the second smallest number is 10.
"""
class Solution(object):
    def findKthNumber(self, n, k):
        if n <= 9 or k == 1: return k
        init, res, sumOfBkts, bktID = 1, 0, [n], 0

        while k > 0:
            k = k-1
            sumOfBkts = self.getBucket(sumOfBkts[bktID], init)
            bktID, k = self.findDigit(sumOfBkts, k)
            res = res*10+(bktID+init) if bktID != 10 else res+1
            init = 0
        return res

    def getBucket(self, togo, init):                  # generate buckets
        if not init: togo -= 1
        L = 9 if init else 10
        newBkt, num, b = [0 for _ in xrange(L)], 1, 0      # num: numbers in this layer  
        while togo > 0:
            add = num if togo-num > 0 else togo             # add the rest numbers into buckets
            newBkt[b], togo, b = newBkt[b]+add, togo-num, b+1
            if b == L: num, b = num*10, 0
        return newBkt

    def findDigit(self, sumBkt, k, bktId=0):                # find out which bucket.
        while k-sumBkt[bktId] >= 0: k, bktId = k-sumBkt[bktId], bktId+1      # go next bucket
        return bktId, k
