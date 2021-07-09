"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
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
        res = []
        self.helper(res, [i for i in xrange(1, n+1)], k)
        return res

    def helper(self, res, nums, k, adding=[]):
        if len(adding) == k:
            res += adding,
            return

        elif len(adding) > k:
            return

        for i in xrange(len(nums)):
            self.helper(res, nums[i+1:], k, adding+[nums[i]])

print Solution().combine(4,2)
