class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # simulate multiplication, handle carry
        #    e.g. 123 x 456
        #      1 2 3     b
        #      4 5 6     a
        #    x -----
        #      7 3 8
        #    6 1 5
        #  4 9 2
        # -----------
        #  5 6 0 8 8

        stash = []
        shift = -1
        for a in num1[::-1]:
            x = int(a)
            tmp = []
            carry = 0
            shift = shift+1
            for b in num2[::-1]:
                y = int(b)
                tmp.append(((x*y)+carry)%10)
                carry = ((x*y)+carry)//10
            
            layer = 0
            for i in range(len(tmp)):
                layer += tmp[i]*pow(10,i)

            stash.append(layer*pow(10,shift))
        
        return sum(stash)

print(Solution().multiply("2","3"))
print(Solution().multiply("123","456"))