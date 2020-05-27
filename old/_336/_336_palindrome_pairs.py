"""
 336. Palindrome Pairs

    Total Accepted: 14792
    Total Submissions: 63412
    Difficulty: Hard
    Contributors: Admin

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # Directly implement: O(n^2) check head & tail before check whole word => TLE
        # Using dictionary, and cut each word into two part: O(n)*O(avglen), Similar to two sum
        worddct, ans = {w[::-1]: i for i, w in enumerate(words)}, []

        # For each word x, seek its counterpart (say y) in dictionary or not.
        for i, w in enumerate(words):
            for j in xrange(len(w)+1):            # cut position from "before 0" to "after -1"
                parta, partb = w[:j], w[j:]
                # check [x, y]
                if parta in worddct and i != worddct[parta] and partb[::-1] == partb:
                    ans += [i, worddct[parta]],
                # check [y, x]
                if partb in worddct and i != worddct[partb] and parta[::-1] == parta and j > 0:
                    ans += [i, worddct[partb]],

        return ans
