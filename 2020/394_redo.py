"""
394
"""
from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        i, k = 0, 0
        while i < len(s):
            # print('i:',i)
            if s[i] in '0123456789':
                k = 10*k+int(s[i])
            elif s[i] == '[':
                j = self.finder(s, i)
                res += k*self.decodeString(s[i+1:j]),
                k = 0
                i = j
            else:
                res += s[i],
            i += 1
        # print(res)
        return ''.join(res)
    
    def finder(self, s, i):
        j = i
        need = 0
        while need < 1:
            j += 1
            if s[j] == '[':
                need -= 1
            elif s[j] == ']':
                need += 1
        return j

print(Solution().decodeString("3[a]2[bc]"), Solution().decodeString("3[a]2[bc]") == "aaabcbc")
print(Solution().decodeString("3[a2[c]]"), Solution().decodeString("3[a2[c]]") == "accaccacc")
print(Solution().decodeString("2[abc]3[cd]ef"), Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
