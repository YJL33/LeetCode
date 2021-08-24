
class Solution:
    def decodeString(self, s):
        res = []
        k = 0

        # find the corresponding right bracket
        # only check bracket
        def finder(start):
            need = 0
            for j in range(start, len(s)):
                if s[j] == ']':
                    if need == 0: return j
                    need -= 1
                elif s[j] == '[':
                    need += 1
            return

        i = 0
        # cases: number, bracket, or alphabets
        while i < len(s):
            if s[i] in '0123456789':
                k = 10*k+int(s[i])
            elif s[i] == '[':
                end = finder(i+1)
                res.append(k*self.decodeString(s[i+1:end]))
                k = 0
                i = end
            else:
                res.append(s[i])
            i += 1
        return ''.join(res)

print(Solution().decodeString("3[a]2[bc]"))