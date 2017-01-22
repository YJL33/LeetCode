"""
115. Distinct Subsequences

Given a string S and a string T,
count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from
the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
class Solution(object):
    def numDistinct(self, original, new):
        """
        :type original: (longer) string
        :type new: (shorter) string
        :rtype: int
        """
        # Define table[i][j] = number of subsequences of original[:i] and new[:j]
        # if original[i] == new[j]:
        #     table[i][j] = table[i-1][j-1] + table[i-1][j]
        # else:
        #     table[i][j] = table[i-1][j]

        len_s = len(original)
        len_n = len(new)

        table = [[0 for i in xrange(len_n+1)] for j in xrange(len_s+1)]

        for i in xrange(len_s):
            table[i][0] = 1

        for i in xrange(1, len_s+1):
            for j in xrange(1, len_n+1):
                if original[i-1] == new[j-1]:
                    table[i][j] += table[i-1][j] + table[i-1][j-1]
                else:
                    table[i][j] += table[i-1][j]

        return table[len_s][len_n]
