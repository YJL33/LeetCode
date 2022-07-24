class Solution:
    def reverseWords(self, s: str) -> str:
        # reverse everything
        self.s = s[::-1]
        # reverse Words
        # handle extra spaces
        
        self.reverser()
        self.removeSideSpaces()
        self.removeRepeatSpaces()
        return self.s

    def removeSideSpaces(self):
        l, r = 0, len(self.s)-1
        while self.s[l] == ' ':
            l += 1
        while self.s[r] == ' ':
            r -= 1
        self.s = self.s[l:r+1]
        # print('self.s:', "=" + self.s + "=")
        return
    
    def reverser(self):
        l, r = 0, 0
        while r <= len(self.s):
            l, r = self.findNextWord(l)
            # print('l, r', l, r)
            tmp = self.s[l:r][::-1]
            self.s = self.s[:l] + tmp + self.s[r:]
            l = r+1
        return

    def findNextWord(self,l):
        r = l+1
        while r < len(self.s) and self.s[r] != ' ':
            r += 1
        return l, r

    def removeRepeatSpaces(self):
        l = 0
        toRmv = set()
        while l+1 < len(self.s):
            if self.s[l] == self.s[l+1] == ' ':
                toRmv.add(l+1)
            l += 1
        res = ''.join([self.s[i] for i in range(len(self.s)) if i not in toRmv])
        self.s = res
        return

print(Solution().reverseWords("Alice does not even like bob"))
print(Solution().reverseWords("  Bob    Loves  Alice   "))