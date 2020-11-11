"""
see https://leetcode.com/problems/zigzag-conversion/
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # intuitive solution
        if numRows == 1: return s
        res = ['' for _ in range(numRows)]

        cnt = 0
        revFlag = False
        for i in range(len(s)):
            res[cnt] += s[i]
            if revFlag:
                cnt -= 1
                if cnt == -1:
                    revFlag = False
                    cnt += 2
            else:
                cnt += 1
                if cnt == numRows:
                    revFlag = True
                    cnt -= 2

        return ''.join(res)

print(Solution().convert("PAYPALISHIRING",3) == "PAHNAPLSIIGYIR")
print(Solution().convert("PAYPALISHIRING",4) == "PINALSIGYAHRPI")
print(Solution().convert("ABC",1) == "A")
