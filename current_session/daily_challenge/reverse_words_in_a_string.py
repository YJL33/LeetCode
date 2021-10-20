# reverse the whole string
# reverse the word itself

class Solution:
    def reverseWords(self, s: str) -> str:
        t = s[::-1]
        ans = []
        # identify next word => reverse and add it into stack
        i = 0
        while i < len(t):
            l, r = i, i
            while l < len(t) and t[l] == ' ':
                l, r = l+1, r+1
            while r < len(t) and t[r] != ' ':
                r += 1
            if l < len(t) and t[l] != ' ': ans.append(t[l:r][::-1])
            # print('ans:', ans)
            i = r
        return ' '.join(ans)

print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("a good    example"))