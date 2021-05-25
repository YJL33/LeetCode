"""
76. Minimum Window Substring

Given a string S and a string T,
find the minimum window in S
which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

Accepted 379,605
Submissions 1,112,525
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # use char dict
        charDict = {}       # required number of character
        for c in t:
            if c in charDict:
                charDict[c] += 1
            else:
                charDict[c] = 1

        missing = len(t)
        i, start, end = 0, 0, 0

        for j, c in enumerate(s, 1):
            if c not in charDict:
                charDict[c] = 0
            missing -= (charDict[c] > 0)
            charDict[c] -= 1

            if not missing:
                while i < j and charDict[s[i]] < 0:
                    charDict[s[i]] += 1
                    i += 1
                if not end or j - i <= end - start:
                    start, end = i, j

        return s[start:end]

print Solution().minWindow("ADOBECODEBANC", "ABC")
print Solution().minWindow("AA", "AA")
