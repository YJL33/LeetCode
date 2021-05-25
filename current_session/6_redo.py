"""
6
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # simply use multiple rows
        if numRows == 1: return s
        rows = ['' for _ in range(numRows)]
        fillingOrders = [0 for _ in range(len(s))]
        x, add = 0, 1
        for i in range(len(s)):
            fillingOrders[i] = x
            if x == numRows-1:
                add = -1
            elif x == 0:
                add = 1
            x += add
        # print fillingOrders, len(fillingOrders), len(s)
        for j in range(len(s)):
            r = fillingOrders[j]
            rows[r] += s[j]
        # print rows

        return ''.join(rows)

print Solution().convert('paypalishiring', 3)
print Solution().convert('paypalishiring', 4)
print Solution().convert('a', 1)
print Solution().convert('abc', 1)