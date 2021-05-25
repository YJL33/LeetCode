"""
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # For a BST(size=3), pick each node as root,
        # the possible number of each root will be BST(size of left)*BST(size of right):
        # F(3) = F(0)*F(2) + F(1)*F(1) + F(2)*F(0)
        # Therefore, F(n) = sum of F(i-1)*F(n-i), for i = 1~n
        res = [1]
        for i in xrange(1,n+1):
            res += 0,
            for j in xrange(1,i+1):
                res[i] += res[j-1]*res[i-j]

        return res[n]
