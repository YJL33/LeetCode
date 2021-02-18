'''
415
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        c1, c2 = len(num1)-1, len(num2)-1
        carry = 0
        while c1 >= 0 and c2 >= 0:
            s = int(num1[c1])+int(num2[c2])+carry
            tmp, carry = s%10, s//10
            res = res+str(tmp)
            c1, c2 = c1-1, c2-1
        
        while c1 >= 0:
            s = int(num1[c1])+carry
            tmp, carry = s%10, s//10
            res = res+str(tmp)
            c1 = c1-1
        while c2 >= 0:
            s = int(num2[c2])+carry
            tmp, carry = s%10, s//10
            res = res+str(tmp)
            c2 = c2-1
        if carry:
            res = res+str(carry)

        # print(res, num1, num2)
        assert(int(res[::-1]) == int(num1)+int(num2))
        return res[::-1]

print(Solution().addStrings('123','321'))