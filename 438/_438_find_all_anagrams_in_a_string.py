"""
438. Find All Anagrams in a String

    User Accepted: 235
    User Tried: 606
    Total Accepted: 280
    Total Submissions: 798
    Difficulty: Easy

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dct = {}
        for c in p:
            if c in dct: dct[c] += 1
            else: dct[c] = 1

        L, res, tmpdct = len(p), [], {}

        for i in xrange(len(s)-L+1):
            if not tmpdct:                            # construct new temp dictionary
                for c in s[i:i+L]:
                    if c not in tmpdct: tmpdct[c] = 1
                    else: tmpdct[c] += 1
            else:                                     # update the dictionary
                tmpdct[s[i-1]] -= 1
                if s[i+L-1] in tmpdct: tmpdct[s[i+L-1]] += 1
                else: tmpdct[s[i+L-1]] = 1
                
            fit = True
            for k in dct.keys():
                if k not in tmpdct or dct[k] != tmpdct[k]:
                    fit = False
                    break
            if fit: res += i,
        
        return res