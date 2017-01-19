"""
151. Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

Clarification:

    What constitutes a word?
    A sequence of non-space characters constitutes a word.
    Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
    How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reverse whole string (just scan backward) and then filp words
        # e.g. "hello world" => "dlrow olleh" => "world hello"
        # Time Complexity: ~O(2n)
        # Space Complexity: ~O(1)
        if not s: return s

        start = len(s)-1                    # eliminate leading spaces
        while s[start] == ' ' and start >= 0:
            start -= 1

        if start == -1: return ''

        end = 0                             # eliminate trailing spaces
        while s[end] == ' ':
            end += 1

        #print "start, end: ", start, end
        last = False
        res = ''
        for i in xrange(start, end-1, -1):  # note that start > end
            #print "now at: ", i
            if s[i] != ' ' and not last:
                #print "assign last = ", i
                last = i
            elif s[i] == ' ' and s[i+1] != ' ':
                res += s[i+1:last+1] + ' '
                last = False
            if i == end:                    # there must be a last in the end
                res += s[end:last+1]

        return res
