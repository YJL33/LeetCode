"""
424

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.

You can perform this operation at most k times.

After performing the above operations,
return the length of the longest substring containing the same letter you can get.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

"""
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = i = 0                          # i = start of window
        count = collections.Counter()           # letter counter, only within window
        for j in range(len(s)):                 # j = end of window
            count[s[j]] += 1
            maxLen = max(maxLen, count[s[j]])
            if j - i + 1 > maxLen + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i