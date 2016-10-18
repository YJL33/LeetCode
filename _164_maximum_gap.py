"""
 164. Maximum Gap

    Total Accepted: 39053
    Total Submissions: 138973
    Difficulty: Hard
    Contributors: Admin

Given an unsorted array,
find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers,
and fit in the 32-bit signed integer range.

For example, given a array [1, 7, 3, 3], the expected result it 4, not (7 - 1) = 6.

We need to sort the the array into [1, 3, 3, 7],
and get the maximum gap between the successive elements in this sorted array, which is (7 - 3) = 4.
"""
import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # required time/space: O(n)
        if len(nums) <= 1: return 0
        snums, maxgap = self.redixSort(nums), 0
        #print "before ", nums
        #print "after ", snums
        
        for i in xrange(1,len(snums)):
            maxgap = max(maxgap, (snums[i]-snums[i-1]))
        return maxgap

    def redixSort(self, nums):
        # implement radix sort
        K = int(math.ceil(math.log(max(nums), 10)))     # we will need K passes
        if math.ceil(math.log(max(nums), 10)) == math.log(max(nums), 10):
            K += 1                                      # special cases: 10^n
        buckets = [[] for _ in xrange(10)]              # buckets of bases (using 10)
        snums = [n for n in nums]
        for i in xrange(1,K+2):                         # K loops
            for n in snums:
                buckets[n%(10**i)/(10**(i-1))] += n,    # put everyone into bucket
            del snums[:]
            #print "buckets: ", buckets
            for b in buckets:
                snums.extend(b)                         # merge buckets as new sorted array
            buckets = [[] for _ in xrange(10)]          # reset buckets
        return snums
