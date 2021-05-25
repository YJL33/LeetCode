"""
387. First Unique Character in a String

Given a string,
find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return -1

        char_dict = {}

        for c in s:
            if c in char_dict:
                char_dict[c] += c,
            else:
                char_dict[c] = [c]

        i = 0
        while i < len(s):
            if len(char_dict[s[i]]) == 1:
                break
            else:
                i += 1

        if i == len(s): return -1
        
        return i
