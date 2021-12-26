class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: return False
        tot = op = cl = 0 # tot -> Total variable brackets, op -> Open, cl -> Closed
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0': tot += 1
            elif s[i] == '(': op += 1
            elif s[i] == ')': cl += 1
            if tot - op + cl < 0: return False
        tot = op = cl = 0
        for i in range(len(s)):
            if locked[i] == '0': tot += 1
            elif s[i] == '(': op += 1
            elif s[i] == ')': cl += 1
            if tot + op - cl < 0: return False 
        return True

print(Solution().canBeValid("())()))()(()(((())(()()))))((((()())(())","1011101100010001001011000000110010100101"), 'should be true')