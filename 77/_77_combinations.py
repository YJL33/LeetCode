"""
77. Combinations

Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # put possible elements into un-fulfilled array.
        cands = [_ for _ in xrange(1,n+1)]
        res = []
        self.helper(k, cands, res)
        
        return res

    def helper(self, left, nums, result, path=[]):
        #print "here we are! (left, nums, res, path)", left, nums, result, path
        if len(nums) < left:
            return
        elif len(nums) == left:
            result.append(path+nums)
            return
        if left == 0:
            result.append(path)
            return

        for i in xrange(len(nums)):
            #print "next path: ", path+[nums[i]]
            self.helper(left-1, nums[i+1:], result, path+[nums[i]])