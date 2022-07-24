from typing import List
class Solution:
    def reverseWords(self, s:List[str]) -> None:
        # reverse whole String
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        
        # find next space to locate each single word
        def nextSpace(i):
            if i >= len(s): return -1
            while i < len(s) and s[i] != ' ':
                i += 1
            # print('next space:', i)
            return i

        # reverse each word
        def reverser(s):
            l, r = 0, nextSpace(0)
            while r != -1:
                tmp, r = r, r-1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l, r = l+1, r-1
                l, r = tmp+1, nextSpace(tmp+1)
            # print('s:', s)
            return

        reverser(s)
        return

print(Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
print(Solution().reverseWords(["a"]))