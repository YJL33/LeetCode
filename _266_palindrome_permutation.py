"""
266. Palindrome Permutation

    Total Accepted: 17566
    Total Submissions: 33041
    Difficulty: Easy

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dct = {}
        for c in s:
            if c in dct: del dct[c]
            else: dct[c] = 1
        if len(s)%2:
            return len(dct) == 1
        else:
            return len(dct) == 0