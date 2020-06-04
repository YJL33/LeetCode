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
        charIndex = {}      # save the index
        for c in t:
            if c in charDict:
                charDict[c] += 1
            else:
                charDict[c] = 1
                charIndex[c] = []

        for i in xrange(len(s)):
            if s[i] in charIndex:
                charIndex[s[i]] += i,

        candidates = []
        for c in charDict.keys():
            # if there's no such window
            if len(charIndex[c]) < charDict[c]:
                return ""
            candidates += charIndex[c]

        # ... so there IS one ...
        # manage 2 pointers
        candidates.sort()
        print candidates
        left, right, minSize = 0, False, len(s)+1

        # find best left
        for i in xrange(len(candidates)-len(t)):

            r = self.getMinWindowSize(s, t, candidates, charDict.copy(), i, minSize)
            print "r: ", r

            if r >= 0:
                minSize = candidates[r]-candidates[i]+1
                left, right = candidates[i], candidates[r]
                print "index - l, r:", i, r
                print "real - l, r:", left, right
        
        return s[left:right+1]

    def getMinWindowSize(self, s, t, candidates, charDict, left, minSize):
        # seek from left to right
        # return r
        missing = len(t)
        r = left
        print "missing, r:", missing, r
        while missing and r<len(candidates) and candidates[r] < candidates[left]+minSize+1:
            char = s[candidates[r]]
            missing -= (charDict[char] > 0)
            charDict[char] -= 1
            print "char(i), missing:", char, r, missing
            if missing: r += 1

        print "l, r: ", left, r, missing
        if not missing:
            return r
        else:
            return -1

# print Solution().minWindow("ADOBECODEBANC", "ABC")
print Solution().minWindow("AA", "AA")
