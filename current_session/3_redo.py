"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Accepted
1,545,427
Submissions
5,123,292
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use sliding window
        maxLen = 0
        length = 0
        start = 0
        charDict = {}

        for i in xrange(len(s)):
            c = s[i]
            # update the start only when c is inside the window
            if c in charDict and start <= charDict[c]:
                start = charDict[c]
                length = i - charDict[c]
            else:
                length += 1
            charDict[c] = i
            maxLen = max(length, maxLen)

        return maxLen

print Solution().lengthOfLongestSubstring("pauifpaiospdvpaoisdpiojpaoiurpa")
# print Solution().lengthOfLongestSubstring("bbbbbb")
# print Solution().lengthOfLongestSubstring("pwwkew")