"""
409. Longest Palindrome

    User Accepted: 9
    User Tried: 12
    Total Accepted: 9
    Total Submissions: 17
    Difficulty: Easy

Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        for c in s:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1

        maxlen, oneodd, maxodd = 0, 0, 0
        for k in dct.keys():
            if not dct[k]%2:
                maxlen += dct[k]
            else:
                oneodd = 1
                maxlen += dct[k]-1

        return maxlen+oneodd