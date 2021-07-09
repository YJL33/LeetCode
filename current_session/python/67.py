'''
67
'''
from collections import Counter
class Solution:
    # def addBinary2(self, a: str, b: str) -> str:
    #     res, carry = [], '0'
    #     for i in range(max(len(a), len(b))):
    #         aa = a[::-1][i] if i < len(a) else '0'
    #         bb = b[::-1][i] if i < len(b) else '0'
    #         c = Counter([aa, bb, carry])
    #         res.append('1' if c['1']%2 else '0')
    #         carry = '1' if c['1']>=2 else '0'

    #     if carry == '1': res.append('1')
    #     return ''.join(res)[::-1]

    def addBinary(self, a: str, b: str) -> str:
        ia, ib = 0, 0
        for i in range(len(a)-1, -1, -1):
            if a[i] == '1':
                ia += 1<<(len(a)-1-i)
        for j in range(len(b)-1, -1, -1):
            if b[j] == '1':
                ib += 1<<(len(b)-1-j)
        return format((ia+ib), 'b')