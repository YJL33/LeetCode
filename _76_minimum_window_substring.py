"""
76. Minimum Window Substring

Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)   # need: required # of each character
        missing = len(t)                # missing: # of characters still missing
        start = end = 0                 # start, end: minimum window
        i = 0                           # i, j: window
        for j, c in enumerate(s, 1):
            missing -= (need[c] > 0)    # if this character is needed => missing-1
            need[c] -= 1                # new character come.
            if not missing:                           # if no missing...
                first = s[i]
                while i < j and need[first] < 0:      # ... we don't need 1st element in the window
                    need[first] += 1                  # => add it back
                    i += 1                            # => and move forward 1 step
                    first = s[i]
                if not end or j - i <= end - start:   # ... 1st time (or update) criteria satisfied
                    start, end = i, j
        return s[start:end]