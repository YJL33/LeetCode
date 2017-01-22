"""
186. Reverse Words in a String II

    Total Accepted: 14857
    Total Submissions: 51169
    Difficulty: Medium

Given an input string, reverse the string word by word.
A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces,
and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
"""
class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        # revese every characters, and reverse each word.
        start, end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start+1, end-1

        cur = 0

        while cur < len(s):
            head = tail = cur
            while s[head] == ' ':
                head, tail = head+1, tail+1
            while tail+1 < len(s) and s[tail+1] != ' ':
                tail += 1
            cur = tail+1
            while head < tail:
                s[head], s[tail] = s[tail], s[head]
                head += 1
                tail -= 1