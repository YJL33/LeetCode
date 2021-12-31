class Solution:
    def findComplement(self, num: int) -> int:
        binaryBaseNum = []
        while num != 1:
            binaryBaseNum.append(num%2)
            num = num//2
        complementNum = []
        for n in binaryBaseNum[::-1]:
            complementNum.append(1-n)
        x = 1
        ans = 0
        for n in complementNum[::-1]:
            ans += n*x
            x = x*2
        return ans