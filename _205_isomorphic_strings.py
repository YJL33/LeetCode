"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character,
while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

Note: You may assume both s and t have the same length.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict, tDict = {}, {}           # To record the mirrors of pattern and word
        for one, two in zip(s, t):
            if one not in sDict:        # If never seen this pattern
                sDict[one] = two        # Add it into dictionary as key, with value = word
            if two not in tDict:        # If never seen this word
                tDict[two] = one        # Add it into dictionary as key, with value = pattern
            if tDict[two] != one or sDict[one] != two:   # Check the mirror
                return False
        return True
