"""
60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.helper(range(1,n+1), k, n, "")


    def helper(self, nums, divider, lefts, res):

        if lefts == 0:
            return res

        comb = 1
        for l in xrange(2,lefts):
            comb *= l

        #print "now: nums:{}, div:{}, lefts:{}, res:{}, comb:{}".format(nums,divider,lefts,res, comb)

        odr = (divider-1)/comb

        if lefts:
            res += str(nums.pop(odr))
            return self.helper(nums, divider%comb, lefts-1, res)
