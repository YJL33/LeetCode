"""
 87. Scramble String

    Total Accepted: 56484
    Total Submissions: 200961
    Difficulty: Hard
    Contributors: Admin

Given a string s1,
we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children,
it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at",
it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
from collections import Counter
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        if Counter(s1) != Counter(s2): return False         # definitely not the case
        for i in xrange(1,len(s1)):
            # the string is not swapped at i, but somehow swapped(?) in other position
            if all(map(self.isScramble, [s1[:i], s1[i:]], [s2[:i], s2[i:]])): return True
            # the string is swapped at i, and may also swapped in other position
            if all(map(self.isScramble, [s1[:i], s1[i:]], [s2[-(i):], s2[:-(i)]])): return True
        return False