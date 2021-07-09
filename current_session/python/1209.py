"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        toRmv, firstRun = [], True
        
        while toRmv or firstRun:
            firstRun = False
            tmp = s
            while toRmv:
                rmv = toRmv.pop()
                tmp = s[:rmv] + s[rmv+k:]
            s = tmp
            for i in range(len(s)-k+1):
                if s[i:i+k].count(s[i]) == k:
                    toRmv += i,
        return s
