"""
 3. Longest Substring Without Repeating Characters

    Total Accepted: 239091
    Total Submissions: 1007165
    Difficulty: Medium
    Contributors: Admin

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin, count, maxcount, pool = 0, 0, 0, {}

        for i in range(len(s)):
            if s[i] not in pool or pool[s[i]] < begin:
                count = count+1
                maxcount = count if count > maxcount else maxcount
            else:
                begin = max(begin, pool[s[i]])
                while begin+1 <= i and s[begin] == s[i]: begin, count = begin+1, i-begin
            pool[s[i]] = i

        return maxcount
