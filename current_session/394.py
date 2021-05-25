"""
394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that:
the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # naive approach: go through from left to right
        # handle cases:
        # 1. non-digits
        # 2. digits
        # 3. brackets

        res = ""
        k = 0
        i = 0

        while i < len(s):
            if s[i] in "0123456789":
                k = 10*k + int(s[i])
                i += 1
            elif s[i] not in "[]":
                res += s[i]
                i += 1
            elif s[i] == "[":
                # find the correct right bracket
                j = self.finder(i, s)
                res += k*self.decodeString(s[i+1:j])
                i = j+1
                k = 0
            else:
                print "?", i, s[i]      # should not have this line printed though
                i += 1

        return res

    def finder(self, i, s):
        j = i+1
        need = 1
        while need > 0 and j < len(s):
            if s[j] == "[":
                need += 1
            elif s[j] == "]":
                need -= 1
            j += 1
        return j-1

print Solution().decodeString("3[a]2[bc]"), Solution().decodeString("3[a]2[bc]") == "aaabcbc"
print Solution().decodeString("3[a2[c]]"), Solution().decodeString("3[a2[c]]") == "accaccacc"
print Solution().decodeString("2[abc]3[cd]ef"), Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"