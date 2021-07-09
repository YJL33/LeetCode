"""
151
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        res = []
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            j = i+1
            while j < len(s) and s[j] != ' ':
                j += 1
            if s[i:j]:
                res += s[i:j],
            i = j+1
        
        # print(res)
        
        return ' '.join(res[::-1])


print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("a good   example"))
print(Solution().reverseWords("  Bob    Loves  Alice   "))