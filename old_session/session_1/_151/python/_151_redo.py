"""
 151. Reverse Words in a String

    Total Accepted: 141210
    Total Submissions: 898175
    Difficulty: Medium
    Contributors: Admin

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reverse whole string and reverse the word back
        if not s: return s

        start = len(s)-1                    # eliminate leading spaces
        while s[start] == ' ' and start >= 0:
            start -= 1

        if start == -1: return ''

        rev, i = [c for c in s[::-1]], 0
        while i < len(rev):
            start = i
            while i != len(rev) and rev[i] != ' ':
                i += 1
            end = i-1
            while start < end:
                rev[start], rev[end] = rev[end], rev[start]
                start, end = start+1, end-1
            i += 1

        while rev[0] == ' ':
            rev.pop(0)
        while rev[-1] == ' ':
            rev.pop()
        cur = 0
        while cur < len(rev):
            if rev[cur] == ' ' and rev[cur+1] == ' ':
                rev.pop(cur)
            else:
                cur += 1

        return "".join(rev)

def main():
    print Solution().reverseWords("the sky is blue"), len(Solution().reverseWords("the sky is blue"))
    print Solution().reverseWords(" 1 "), len(Solution().reverseWords(" 1 "))
    print Solution().reverseWords("  a    b   "), len(Solution().reverseWords("  a    b   "))

if __name__ == "__main__":
    main()