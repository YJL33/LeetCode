"""
see https://leetcode.com/problems/basic-calculator/
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c in '+-':
                res += sign*num
                num = 0
                sign = [-1, 1][c == '+']
            elif c == '(':
                stack += (res,sign),
                sign, res = 1, 0
            elif c == ')':
                # print(num,stack)
                prev_res, prev_sign = stack.pop()
                res += sign*num
                res *= prev_sign        # things inside bracket should * prev_sign
                res += prev_res
                num = 0

        return res + num*sign

print(Solution().calculate("(1+(4+5+2)-3)+(6+8)") == (1+(4+5+2)-3)+(6+8))
print(Solution().calculate("1-(5)") == 1-(5))
print(Solution().calculate("1+1+1+(1-1+1-1+1-1-1+1+1+1+1-1-1-1-1-1-1+1+1+1)+(1+1)+(1+(1+(1-1+1-1+1)+(1+1)+1)+1)") == 1+1+1+(1-1+1-1+1-1-1+1+1+1+1-1-1-1-1-1-1+1+1+1)+(1+1)+(1+(1+(1-1+1-1+1)+(1+1)+1)+1))