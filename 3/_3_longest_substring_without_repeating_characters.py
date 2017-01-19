"""
3. Longest Substring Without Repeating Characters

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
        start = maxLength = 0
        usedChar = {}

        for i in xrange(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:    # If the char is in the substring
                start = usedChar[s[i]] + 1                      # Update the start
            else:
                maxLength = max(maxLength, i - start + 1)       # Update the maxlength

            usedChar[s[i]] = i              # Record the char

        return maxLength