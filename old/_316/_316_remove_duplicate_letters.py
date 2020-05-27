"""
 316. Remove Duplicate Letters

    Total Accepted: 21375
    Total Submissions: 76870
    Difficulty: Hard
    Contributors: Admin

Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appear once and only once.

You must make sure your result is the smallest in lexicographical order among all possible results.

Example:

Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        rindex = {c: i for i, c in enumerate(s)}        # last position shown in s
        result = ''
        for i, c in enumerate(s):                       # Add by order of original string
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]                # remove invalid ones before addition
                result += c
        return result

    def removeDuplicateLetters1(self, s):
        result = ''
        while s:
            i = min(map(s.rindex, set(s)))      # Get the first apprearance among all r-indices
            c = min(s[:i+1])                    # Get the 1st lexicographical letter before i
            result += c                         # Add it into result, 
            s = s[s.index(c):].replace(c, '')   # and remove un-necessary parts from s
        return result

    def removeDuplicateLetters2(self, s):
        for c in sorted(set(s)):                # Add by lexicographical order.
            suffix = s[s.index(c):]             # substring after it's first appearance
            if set(suffix) == set(s):           # if same set => deal with the rest letter
                return c + self.removeDuplicateLetters2(suffix.replace(c, ''))
        return ''

