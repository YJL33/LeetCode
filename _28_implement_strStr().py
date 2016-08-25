"""
28. Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # brute force method
        if not needle: return 0

        nlen = len(needle)
        hlen = len(haystack)
        cursor = 0

        for i in xrange(0,hlen-nlen+1):
            while cursor < nlen and haystack[i+cursor] == needle[cursor]:
                cursor += 1
            if cursor == nlen:
                return i
            else:
                cursor = 0

        return -1