"""
3. Longest Substring Without Repeating Characters
Medium

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
1,482,986
Submissions
4,945,702
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window?
        maxLen = 0
        left, right = 0, 0
        charDict = {}
        for i in xrange(len(s)):
            if s[i] in charDict and left <= charDict[s[i]]:
                left = charDict[s[i]]+1
            right = i+1
            charDict[s[i]] = i
            # print left, right, i, s[left:right]
            maxLen = max(maxLen, right-left)
            # print maxLen


        return maxLen


            

print Solution().lengthOfLongestSubstring("apsodifupbjapsdijfpa")