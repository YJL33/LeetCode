"""
395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string
(consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3
Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input:
s = "ababbc", k = 2
Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        
        dct, ng = {}, []                # count the appearance of elements in all string
        for i in xrange(len(s)):
            if s[i] in dct:
                dct[s[i]] += i,         # record index of each element
            else:
                dct[s[i]] = [i]

        for key, val in dct.items():    # check whether is there existing any invalid element
            if len(val) < k:
                ng += val               # if existing, the index will be separator

        if ng == []:                    # if not existing any, just return the whole substring
            return len(s)
        else:                           # else, separate the string with these invalid elements
            res, ng = 0, [-1]+ng+[len(s)]           # add two more separator at both end
            for j in xrange(len(ng)-1):
                res = max(res, self.longestSubstring(s[ng[j]+1:ng[j+1]], k))
            return res