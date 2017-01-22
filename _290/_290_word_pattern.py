"""
290 Word Pattern
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters,
and str contains lowercase letters separated by a single space.

Reference:
http://goo.gl/djJsy1
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        ptnDict, wordDict = {}, {}      # To record the mirrors of pattern and word
        for ptn, word in zip(pattern, words):
            if ptn not in ptnDict:      # If never seen this pattern
                ptnDict[ptn] = word     # Add it into dictionary as key, with value = word
            if word not in wordDict:    # If never seen this word
                wordDict[word] = ptn    # Add it into dictionary as key, with value = pattern
            if wordDict[word] != ptn or ptnDict[ptn] != word:   # Check the mirror
                return False
        return True
