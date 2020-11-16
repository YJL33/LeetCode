"""
https://leetcode.com/problems/basic-calculator-ii/
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use stack
        if not s: return 0
        stack, num, sign = [], 0, '+'

        for i in range(len(s)):
            if s[i] in '0123456789':                    # see the number
                num = num*10 + int(s[i])
            if s[i] in '+-*/' or i == len(s)-1:         # meet the next operator
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    ss = (-1) if tmp < 0 else 1
                    stack.append(ss* (abs(tmp)/num))
                sign = s[i]
                num = 0
        return sum(stack)