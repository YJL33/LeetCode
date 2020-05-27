"""
168. Excel Sheet Column Title

Given a positive integer,
return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # implement 26-cimal
        res = ''
        while n != 0:
            rmd = (n-1)%26+1
            res, n = chr(rmd+64) + res, (n-rmd)/26

        return res