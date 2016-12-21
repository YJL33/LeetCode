"""
 327. Count of Range Sum

    Total Accepted: 13724
    Total Submissions: 48021
    Difficulty: Hard
    Contributors: Admin

Given an integer array nums,
return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between i, j (i <= j), inclusive.

Note:
A naive algorithm of O(n^2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""
import bisect
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # applying mergesort: elements in right > left.
        # for all element in l, count how many r in right satifsy: lower <= r-l <= upper
        def msort(lo, hi):

            mid = lo + (hi-lo)/2
            if mid == lo: return 0
            count = msort(lo, mid) + msort(mid, hi)
            for l in psum[lo:mid]:                                  # lower+l <= r <= upper+l
                count += seek(l, mid, hi)
            psum[lo:hi] = sorted(psum[lo:hi])

            return count

        def seek(left, mi, mx):
            # Search the minimum p and q, which satisfy:
            # lower <= psum[p]-left (valid)
            # upper < psum[q]-left  (invalid)
            # then return (q-p), which is the number of valid range sums.
            p = bisect.bisect_left(psum, left+lower, mi, mx)
            q = bisect.bisect_right(psum, left+upper, mi, mx)

            return q-p

        # partial sum: psum[i] = the sum of all numbers before index i
        # now, difference of two elements in psum (e.g. psum[i] and psum[j]) == range sum i to j
        psum = [0]
        for n in nums:
            psum.append(psum[-1]+n)         # here additional [0] is good => to examine i == jS

        return msort(0, len(psum))