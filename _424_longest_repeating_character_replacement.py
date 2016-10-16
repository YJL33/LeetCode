"""
424. Longest Repeating Character Replacement

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

Given a string that consists of only uppercase English letters,
you can replace any letter in the string with another letter at most k times.
Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        table = {}
        res, p1, p2 = 0, 0, 0
        while p2 < len(s):
            table[s[p2]] = table.get(s[p2], 0) + 1
            p2 += 1
            
            while sum(table.values()) - max(table.values()) > k:
                table[s[p1]] -= 1
                p1 += 1
                
            res = max(res, p2 - p1)
        
        return res