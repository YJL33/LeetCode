class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l, m = len(a), len(b)
        carry = 0
        res = []
        for i in range(max(l,m)):
            if i < l: carry += int(a[~i])
            if i < m: carry += int(b[~i])
            if carry == 0:
                res.append("0")
                carry = 0
            elif carry == 1:
                res.append("1")
                carry = 0
            elif carry == 2:
                res.append("0")
                carry = 1
            else:
                res.append("1")
                carry = 1
        if carry: res.append("1")
        return "".join(res[::-1])