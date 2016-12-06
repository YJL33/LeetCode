"""
214. Shortest Palindrome

    Total Accepted: 31301
    Total Submissions: 138416
    Difficulty: Hard
    Contributors: Admin

Given a string S, convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reverse and compare with original string, using i & j as index.
        # if match => i+1 & j+1
        # else => add the needed substring in reversed string into answer, reset i (or not).
        rev, i, j, lm = s[::-1], 0, 0, 0        # lm: records position of last match
        add, radd = "", ""
        while i+j < len(s)-1:
            if s[i] == rev[j]: i, j = i+1, j+1  # MATCH
            elif (lm == 0) and all(rev[j] == rev[i] for i in range(lm, j)):     # NOT MATCH
                radd += rev[j]                  # special case: repetitve leading character
                j, lm = j+1, j+1                # (don't reset i)
            else:                               # NOT MATCH
                if radd: radd, lm = "", 0       # (cancel prior special case if exist)
                for k in range(lm, j+1):        # additional substring: rev[lm:j+1]
                    add += rev[k]               # check better solution before adding any substring
                    if rev[k] == s[i] and add+s == (add+s)[::-1]: return add+s
                i, j, lm = 0, j+1, j+1
        return add+s if radd == "" else radd+s