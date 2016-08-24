"""
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(s):
            if s[::-1][i] == ' ':
                i += 1
            else:
                break

        for ch in s[::-1][i:]:
            if ch == ' ':
                break
            else:
                count += 1

        return count