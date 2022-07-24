class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # simply implement straight multiply
        #     1 2 3
        #       4 5
        #    ------
        #     6 1 5
        #   4 9 2
        # ---------
        #   5 5 3 5
        res = 0
        t = 1
        for i in range(len(num2)-1, -1, -1):
            x = self.helper(num2[i], num1)
            # print("x*t:", x*t)
            res += x*t
            t *= 10
        return str(res)

    def helper(self, n, num1):
        # print('n:', n, "num1", num1)
        n = int(n)
        carry = 0
        ans = 0
        t = 1
        for j in range(len(num1)-1, -1, -1):
            m = int(num1[j])
            ans += ((n*m + carry)%10) * t
            carry = (n*m + carry)//10
            t *= 10
        if carry != 0: ans += (carry*t)
        # print('ans:', ans)
        return ans

print(Solution().multiply("123","45"))
print(Solution().multiply("123456789","987654321"))